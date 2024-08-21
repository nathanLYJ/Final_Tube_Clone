from django.shortcuts import render
from .models import Post
from .forms import PostForm


# def index(request):
#     posts = Post.objects.all()
#     form = PostForm()
#     return render(request, "main/index.html", {"posts": posts, "form": form})


def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # 유효성 검사 통과 시 처리
            pass
    else:
        form = PostForm()
    return render(request, "main/index.html", {"posts": posts, "form": form})
