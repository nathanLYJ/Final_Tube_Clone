# FBV: Function Based View

# from django.db import models
# from django.contrib.auth.models import User


# class Post(models.Model):
#     title = models.CharField(max_length=100)  # 최대 길이 100
#     content = models.TextField()
#     thumbnail_image = models.ImageField(
#         upload_to="blog/images/%Y/%m/%d/", blank=True
#     )  # blank=True: 필수가 아님
#     video_file = models.FileField(
#         upload_to="blog/files/%Y/%m/%d/", blank=True
#     )  # blank=True: 필수가 아님
#     view_count = models.IntegerField(default=0)  # 조회수
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )  # auto_now_add=True: 생성 시간이 자동으로 업데이트됨
#     updated_at = models.DateField(
#         auto_now=True
#     )  # auto_now=True: 수정 시간이 자동으로 업데이트됨
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE
#     )  # User, on_delete=models.CASCADE user가 삭제(on_delete)되면 post도 삭제(CASCADE)
#     tags = models.ManyToManyField("Tag", blank=True)  # Tag, blank=True 태그는 없어도 됨

#     def __str__(self):
#         return self.title


# class Comment(models.Model):
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#     post = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name="comments"
#     )  # Post, on_delete=models.CASCADE post가 삭제(on_delete)되면 comment도 삭제(CASCADE)
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE
#     )  # User, on_delete=models.CASCADE user가 삭제(on_delete)되면 comment도 삭제(CASCADE)

#     def __str__(self):
#         return self.message


# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name


# class Subscription(models.Model):
#     subscriber = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="subscriptions"
#     )
#     channel = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="subscribers"
#     )
#     subscribed_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ("subscriber", "channel")  # 구독자와 채널은 유일해야 함

#     def __str__(self):
#         return f"{self.subscriber.username}이 {self.channel.username}를 구독하였습니다."
############################################################################################

# CBV(Class Based View) 방식으로 구현한 회원가입, 로그인, 로그아웃, 프로필 페이지 뷰
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumb_image = models.ImageField(upload_to="tube/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="tube/files/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/tube/{self.pk}/"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
