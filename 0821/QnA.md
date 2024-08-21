```python
###################################

유효성 검사
    - 1. Front-end에 유효성 검사
    - 2. Django Forms에 유효성 검사
    - 3. Django Views에 유효성 검사
    - 4. Django Models에 유효성 검사
    - DRF 유효성 검사(아직 안배웠기 때문에)

###################################

tailwind

###################################

mkdir qna
cd qna
python -m venv venv
.\venv\Scripts\activate
pip install django
django-admin startproject config .
python manage.py migrate

###################################

python manage.py startapp main

###################################

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]

###################################
# config/urls.py

from django.contrib import admin
from django.urls import path
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

###################################
# main/views.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")


###################################
# main/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

###################################

python manage.py makemigrations
python manage.py migrate

###################################

from django.contrib import admin
from .models import Post

admin.site.register(Post)

###################################

python manage.py createsuperuser
leehojun
leehojun@gmail.com
dlghwns1234!

###################################

python manage.py runserver

게시물 4개 등록

1 11 111
2 22 222
3 33 333
11 123 123

###################################

# main > views.py
from django.shortcuts import render
from .models import Post


def index(request):
    post = Post.objects.get(pk=2)  # 아까 delete해서 pk=1이 없어져서 pk=2로 변경
    return render(request, "main/index.html", {"post": post})

###################################
# main > templates > main > index.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <title>템플릿 필터 명령어</title>
</head>
<body>
   
</body>
</html>

###################################
# main > forms.py

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

###################################
# main > views.py

from django.shortcuts import render
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(request, "main/index.html", {"posts": posts, "form": form})


###################################

1. Front-end에 유효성 검사

###################################
# main > templates > main > index.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <title>템플릿 필터 명령어</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">작성</button>
    </form>
    <hr>
    <ul>
        {% for post in posts %}
            <li>{{ post.title }} - {{ post.content }}</li>
        {% endfor %}
    </ul>
    <script>
        // 굳이 유효성 검사를?
        // 서버에 들어오기 전에 유효성 검사를 해주시면
        // 서버에 부하를 줄일 수 있습니다.
        // 서버에서 들어오는 데이터를 어느정도 필터링도 가능합니다.
    </script>
</body>
</html>


###################################


다음 코드에 유효성 검사를 javascript로 할거야. 이 유효성 검사에는 기본 유효성 검사가 들어가고 다음과 같은 추가 유효성 검사가 들어가야해.

제목은 3자 이상, 100자 이하여야해.

<form method="post">
    <p>
        <label for="id_title">Title:</label>
        <input type="text" name="title" maxlength="100" required="" id="id_title">
    </p>
    <p>
        <label for="id_content">Content:</label>
        <textarea name="content" cols="40" rows="10" required="" id="id_content"></textarea>
    </p>
    <button type="submit">작성</button>
</form>

답변:

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const titleInput = document.getElementById('id_title');
    const contentInput = document.getElementById('id_content');

    form.addEventListener('submit', function(event) {
        let isValid = true;
        let errorMessage = '';

        // 제목 유효성 검사
        if (titleInput.value.length < 3 || titleInput.value.length > 100) {
            isValid = false;
            errorMessage += '제목은 3자 이상 100자 이하여야 합니다.\n';
        }

        // 내용 유효성 검사 (비어있지 않은지 확인)
        if (contentInput.value.trim() === '') {
            isValid = false;
            errorMessage += '내용을 입력해주세요.\n';
        }

        if (!isValid) {
            event.preventDefault();
            alert(errorMessage);
        }
    });
});

###################################

# 위 코드를 html에 추가하면 됩니다.
# 수업에서는 반영하진 않습니다. 코드 복잡도가 올라가기 때문입니다.

###################################

2. Django Forms에 유효성 검사

###################################