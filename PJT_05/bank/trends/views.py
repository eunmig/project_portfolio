from django.shortcuts import render, redirect
from .models import Trend, Keyword
from .forms import KeywordForm, TrendForm
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd


# Create your views here.
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
            form = KeywordForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'form': form,
        'keywords' : keywords
    }
    return render(request, 'trends/keyword.html', context)



def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')  


def crawling(request):
    keywords = Keyword.objects.all()
    trends = Trend.objects.all()

    trends.delete()

    for word in keywords:
        url = f'https://www.google.com/search?q={word.name}'
        
        # 크롬 브라우저가 열림
        # 이 때, 동적인 내용들이 모두 채워진다!
        driver = webdriver.Chrome()
        driver.get(url)

        # 열린 페이지 소스를 받아옴
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # 검색 결과 가져오기
        # div 태그 안의 id 가 result-stats 라는 요소
        result_stats = soup.select_one("div#result-stats")
        text_crawling = result_stats.text
        
        # 개수 추출 작업
        text2 = text_crawling.split()
        text3 = text2[2]

        result2 = text3.split(',')
        result3 = ''.join(result2)
        result4 = result3.split('개')
        result5 = result4[0]

        result6 = int(result5) // 1e5

        # Trend Table에 저장
        
        trend = Trend(
            name = word.name,
            result = result6,
            search_period = text3, 
        )
        trend.save()



    context = {
        'trends' : trends,
        'keywords' : keywords
    }
    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    trends = Trend.objects.all()

    # 출력할 딕셔너리
    histo_name = []
    histo_result = []
    for word in trends:
        histo_name.append(word.name)
        histo_result.append(word.result)


    plt.clf()

    
    # bar형태의 그래프를 그려줌
    plt.bar(histo_name, histo_result)
    plt.grid(True)
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result(1e5)')

    # 임시 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '') 
    buffer.close()
    context = {
        'chart_histo':f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    context = {
    }
    return render(request, 'trends/crawling_advanced.html', context)

