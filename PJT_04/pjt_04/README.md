# project 04
팀원: 송의찬, 이민지, 박은미
## 1. 메인페이지
- 로그인 전/후 의 메인페이지 작성
- 부트스트랩을 사용해 네비게이션 생성
#### 밖에 있는 base.html에 네비게이션 코드 받아 수정

    1.1 원래 코드의 리스트를 사용하지 않고 a 태그를 통해 버튼 작성, a태그를 써서 나오는 밑의 밑줄은 스타일태그에서 a {
        text-decoration: none;
      }
      를 넣어 삭제했다.
    1.2 a 태그의 링크들은 각 페이지들에서 만든 url들을 따왔다.
## 2. 영화 작성 페이지
- create.html 생성
- title, description, 제출 버튼
#### 실습 10_3에서 만든 코드들을 따와 이름만 바꿔줬다
    2.1 form태그 사용해 create.html을 만들었다

## 3. 상세 페이지
- 영화 제목, 내용 보여주고
- update버튼, delete버튼 제작
- back 버튼 제작
#### create에서 만든 페이지를 수정하기 위해 detail 만듬
    3.1 form 태그 사용해 method, url 받고
    3.2 버튼을 제작해야 해서 버튼에서 onclick으로 url 연결했다
    3.3 버튼 색깔은 부트스트랩 코드를 사용했다
    3.4 delete 버튼의 타입은 submit으로 해서 for문의 url을 받았다
## 4. 영화 수정 페이지
- 작성했던 title, description 변경 가능
#### update 만듬
    4.1 원래 코드에서 이름만 바꿔줬다
## 5. 로그인 페이지
- 로그인 가능한 페이지
#### login 만듬
    5.1 역시 원래 코드에서 이름만 바꿔줬다
## 6. 회원가입 페이지
- accounts의 forms.py 에서 field에 'username', 'email','first_name', 'last_name' 넣어 원하는 것만 입력할 수 있게 함
#### accounts의 forms.py에서 만듬
    6.1 CustomUserCreationForm 클래스를 만들었다
    6.2 field에 'username', 'email','first_name', 'last_name' 넣어 원하는 것만 입력할 수 있게 함
## 7. 회원 정보 수정 페이지
- 원래 나오는 비밀번호를 변경하는 폼 링크를 제거 
#### accounts의 forms.py에서 만듬 
    7.1 CustomUserChangeForm 클래스 만들었다
    7.2 field에 'email','first_name', 'last_name', 'username' 넣어 원하는 것만 입력할 수 있게 함
    7.3 장고에서 제공하는 비밀번호 변경폼 (help_Text)을 지우고자 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필드에 있는 help_text를 숨깁니다.
        for field_name in self.fields:
            self.fields[field_name].help_text = None
        # 비밀번호가 설정되지 않습니다. 삭제
        del self.fields['password']
    넣어줌
## 8. 비밀번호 수정 페이지
- 회원정보 수정에서 나오던 비밀번호 변경 폼 링크를 버튼으로 생성
#### change_password 만듬, update에 넣어줌
    8.1 form 태그 사용해서 update에 넣어줌
