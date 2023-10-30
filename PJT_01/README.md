# 본인의 API_KEY 잘 보관하기

# URL에서 .json 형태로 요청하기
    def ----():
        api_key = ""
        
        rl =  f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1'
        response = requests.get(url).json()
        result = response[].----()

        return result

# problem1
처음에 공식문서에 정보를 요청해 응답받기까지 시행착오를 거침.
전날 7월20일 실습문제를 풀어본 기억을 더듬어 실습문제의 코드를 참고하여 작성해봄.

# problem2
problem1에 요청하는 변수만 수정하여 결과값 도출.