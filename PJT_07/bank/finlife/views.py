
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import ProductsSerializer, OptionsSerializer
from .models import DepositOptions, DepositProducts

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    bank_list = requests.get(url).json()



    # result = bank_list['result'].keys()
    return Response(bank_list)


@api_view(['GET'])
def save_DP(request):
    api_key = settings.API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    bank_list = requests.get(url).json()

    # bank_list에서 models에 필요한 데이터 가져오기
    for li in bank_list.get('result').get('baseList'):
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note': li.get('etc_note'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
        }

        serializer = ProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    for li in bank_list.get('result').get('optionList'):

        # 변수에 fin_prdt_cd 저장하기
        fin_prdt_cd = li.get('fin_prdt_cd')
        
        # product 변수에 optionList와 DepositProducts에서 fin_prdt_cd가 일치하면, product 아이템하나를 저장
        product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)

        intr_rate = li.get('intr_rate')
        if intr_rate is None:
            intr_rate = -1

        intr_rate2 = li.get('intr_rate2')
        if intr_rate2 is None:
            intr_rate2 = -1

        # product의 pk를 '할당' 하기.
        save_data = {
            'product': product.pk,
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate': intr_rate, 
            'intr_rate2': intr_rate2, 
            'save_trm': li.get('save_trm'),
        }

        serializer = OptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message': 'Data saved successfully'})


# 요청사항이 'GET'이라면, DepositProducts의 모든 정보를 요청하여 조회하기
# 요청사항이 'POST'라면, DepositProducts가 정보가 생성되는지 확인
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        finlifes = DepositProducts.objects.all()
        serializer = ProductsSerializer(finlifes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 상품 리스트의 pk값과 options pk 값이 일치하면 pk의 옵션들 모두 출력 
@api_view(['GET'])
def deposit_PO(request, fin_prdt_cd):
    option_list = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = OptionsSerializer(option_list, many=True)
    return Response(serializer.data)


def top_rate(request):
    options = DepositOptions.objects.all()

    # 금리가 없는 경우 default 값 -1을 저장했기 때문에, DB 내에서 최저 값임
    max_intr_rate = -1 

    top_option = None 
    top_product = None 

    # 가져온 options 아이템에서 최고 값을 찾고, 최고 값을 찾으면 해당 option으로 갱신
    for option in options:
        if option.intr_rate > max_intr_rate:
            max_intr_rate = option.intr_rate
            top_option = option

    # top_option 에 속한 외래키 product를 새로운 아이템으로 지정.
    top_product = top_option.product

    option_serializer = OptionsSerializer(top_option)
    product_serializer = ProductsSerializer(top_product)
    # 해당 데이터 반환
    response_data = {
        'deposit_product': product_serializer.data,
        'options': option_serializer.data,
    }

    return JsonResponse(response_data)
