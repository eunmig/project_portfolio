from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields =('username', 'email','first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        
        fields = ('email','first_name', 'last_name', 'username')

    # # 비밀번호 변경시 폼 링크 제공하는 helptext 제거
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필드에 있는 help_text를 숨깁니다.
        for field_name in self.fields:
            self.fields[field_name].help_text = None
        # 비밀번호가 설정되지 않습니다. 삭제
        del self.fields['password']
        
        

