# FBV: Function Based View

# from django.urls import path
# from . import views

# # login, logout 이름 사용 X

# urlpatterns = [
#     path("signup/", views.user_signup, name="user_signup"),
#     path("login/", views.user_login, name="user_login"),
#     path("logout/", views.user_logout, name="user_logout"),
#     path("profile/", views.user_profile, name="user_profile"),
# ]

#################################################################################################################
# CBV: Class Based View

from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
