## 정휘원/박은미 조
---
### 일정표

- 11:00 ~ 12:00
1. 정휘원 - 기본 코드 작성, urls/views 등 만들 코드들 정리
2. 박은미 - 수업 내용 정리 -> 프로젝트와 연관 코드들

- 13:00 ~ 13:30
1. 정휘원/박은미 - 과제 A 이해 후 코드 작성, models 변경 등

- 13:30 ~ 14:30
1. 정휘원 - 과제B 코드 작성, git branch 분기 생성
2. 박은미 - 과제C 코드 작성

- 14:30 ~ 15:00
1. 정휘원/박은미 - 상호 코드 점검 및 이해, 이후 프로젝트 진행

- 15:00 ~ 16:00
1. 정휘원 - 과제 E 코드 작성
2. 박은미 - 과제 D 코드 작성
3. 정휘원/박은미 - 코드 리뷰

- 16:00 ~ 16:30
1. 최종 코드 점검 및 README 추가 작성, 제출

---
### 고난과 역경
1. 과제 A(휘원/*은미*) - bank pjt 처음으로 할 때와 django, DB sql과 REST 까지 모두 합쳐서 개념을 처음 이해하는 것이 어려웠음.
역할을 나눠 수업코드를 우리 코드에 적용시킬 방법을 찾는 것과, 기본적으로 시간이 걸리는 틀짜기를 시행했다.

2. 과제 B, C(은미) - 데이터를 전송 할 때 원하는 데이터가 DB에 저장되지않았다. 
```
# ProductsSerializer 데이터를 DB에 전송하고 싶었는데 OptionsSerializer을 입력해 놓고 안되는 이유를 찾고 있었다.

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

```

3. 과제 D(은미) - views.py를 작성 후 서버를 실행했더니 PAGE NOT FOUND error가 발생했다.
함수 작성의 문제인줄... pk를 잘 못 받아온줄 알고 수정했지만 결국은 urls.py에 오타가 나서 page를 못찾고 있었다.
```
# <str:fin_prdt_cd>/ url을 잘 작성하자.

urlpatterns = [
    path('', views.index),
    path('save-deposit-products/', views.save_DP),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_PO),
    path('deposit-products/top_rate', views.top_rate),
]

```

4. 과제 E(휘원) - 이전 코드들 작성을 통해 실질적으로 약 5분만에 작성하고 완료했다.

---

향후 프로젝트에 대해 어떤 방식으로 접근하고 어떤 팀워크를 펼쳐야하는지에 대한 감을 잡을 수 있었다.
생각보다 맞춘 시간이 널널했고, 개인 코딩과 리뷰시간의 적절한 비율이 중요하다고 느꼈다.