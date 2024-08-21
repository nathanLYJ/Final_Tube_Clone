# FBV 방식으로 구현한 URL 패턴을 CBV 방식으로 변경하기
#  from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.tube_list, name="tube_list"),
#     path("<int:pk>/", views.tube_detail, name="tube_detail"),
#     path("create/", views.tube_create, name="tube_create"),
#     path("<int:pk>/update/", views.tube_update, name="tube_update"),
#     path("<int:pk>/delete/", views.tube_delete, name="tube_delete"),
#     path("tag/<str:tag>/", views.tube_tag, name="tube_tag"),
#     # comment 삭제 url 추가
#     path("<int:pk>/comment_delete/", views.tube_comment_delete, name="tube_comment_delete"),
# 	    path(
#         "<int:pk>/comment_delete/",
#         views.tube_comment_delete,
#         name="tube_comment_delete",
#     ),
#     # 구독 url 추가
#     path(
#         "<int:post_id>/<int:user_id>/subscribe/",
#         views.tube_subscribe,
#         name="tube_subscribe",
#     ),
#     # 구독 취소 url 추가
#     path(
#         "<int:post_id>/<int:user_id>/unsubscribe/",
#         views.tube_unsubscribe,
#         name="tube_unsubscribe",
#     ),
# ]

# CBV 방식으로 변경한 URL 패턴을 app_name을 사용하여 namespace를 지정하기
# tube > urls.py

from django.urls import path
from . import views

app_name = "tube"
# app_name = "tube" 추가하는 이유는 tube:post_list 이런식으로 사용하기 위함
# {% url 'tube:post_list' %}
# {% url 'tube:post_detail' post.pk %}

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("<int:pk>/delete/", views.post_delete, name="post_delete"),
]
