# PJT-5 김태경 박은미

## Problem A

base.html 파일 생성 후 project의 settings.py에 등록을 해야된다.



## Problem B

DB에 데이터가 저장되었지만, 서버에서 출력되지 않았다.
keywords = Keyword.objects.all()로 받아왔지만
keyword로 잘못 입력해서 정상적인 출력이 되지 않았다.



## Problem C

Keyword Table에 저장된 데이터와 크롤링한 데이터를 하나의 테이블로 합쳐서 html로 넘겨주어야 했는데,

 Trend에 새로 저장을 해 줘야 크롤링이 정상적으로 작동했다.



```
keywords = Keyword.objects.all()
trends = Trend.objects.all()

trends.delete()

for word in keywords:
    ...(크롤링)
    
    # 개수 추출 작업
    ...(전처리)

    result6 = int(result5) // 1e5

    # Trend Table에 저장
    
    trend = Trend(
        name = word.name,
        result = result6,
        search_period = text3, 
    )
    trend.save()

```


## Problem D

result의 데이터 전처리를 너무 큰 수(1e9)로 나누자
0으로만 저장되어 잘못 전처리를 하였다.


이를 수정하기 위해 적당한 수(1e5)로 변경하였고 정상출력되었다.