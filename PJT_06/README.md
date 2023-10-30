# PJT_06
## 조원 : 정휘원(포르쉐), 박은미


## A. 유저기능
user 모델을 커스텀하여 필요한 데이터를 개발자가 수정, 작성 할 수 있도록 작성
```
# forms.py

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```


## B. Boards 앱 기능
수정, 삭제 기능의 본인이 작성한 게시글이였을때만 기능이 동작하도록 작성
```
# views.py

@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        # 인증된 사용자만 delete 가능
        if request.user.is_authenticated:
            if request.user == board.author:    
                board.delete()
                return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    comments = board.comments.all()
    comment_form = CommentForm()
    
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)


# detail.html

{% if user == board.author %}
<a href="{% url 'boards:update' board.id %}"><button class="me-3 btn btn-success">수정하기</button></a>
<form action="{% url 'boards:detail' board.id%}" method='POST'>
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">삭제하기</button>
</form>
{% endif %}

```


## C. 프로필 페이지
프로필 페이지를 생성하고 페이지 작성
```
# views.py

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)
```

## D. 유저 팔로우 기능
인증된 사용자만 다른 사용자를 팔로우 할 수 있으며, 사용자는 자기 자신을 팔로우 할 수 없다.
```
# profile.html

{% if request.user != person %}
<div style="display: flex; justify-content: space-between; align-items: center;">
    <form action="{% url 'accounts:follow' person.pk %}" method='POST' style="margin-left: auto;">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
            <input type="submit", value='Unfollow'>
        {% else %}
            <input type="submit", value='Follow'>
        {% endif %}
    </form>
</div>
{% endif %}
```


# E. 게시글 좋아요 기능
인증된 사용자만 좋아요 버튼과 좋아요 개수 표시
```
# index.html

    <form action="{% url 'boards:likes' board.pk%}" method="POST">
      {% csrf_token %}
      # 인증된 사용자만 좋아요 기능 사용 가능
      {% if request.user in board.like_users.all %}
      <input type="submit" value='좋아요 취소' class='btn btn-primary btn-sm'>
      # 좋아요 버튼과 좋아요 개수 표시
      <p>{{ board.like_users.all|length }}명이 이 리뷰를 좋아합니다</p>
      {% else %}
      <input type="submit" value='좋아요' class='btn btn-secondary btn-sm'>
      {% endif %}
    </form>

```