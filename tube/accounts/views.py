# FBV(Function Based View) 방식으로 구현한 회원가입, 로그인, 로그아웃, 프로필 페이지 뷰
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import login, logout, authenticate
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required


# # Create your views here.
# def user_signup(request):
# 	if request.method == 'POST':

# 		username = request.POST['username']
# 		password = request.POST['password']
# 		email = request.POST.get('email','')

# 		if not (username and password):
# 			return HttpResponse('이름과 패스워드는 필수입니다!')

# 		if User.objects.filter(username=username).exists():
# 			return HttpResponse('이미 존재하는 사용자입니다!')
# 		if email and User.objects.filter(email=email).exists():
# 			return HttpResponse('이미 존재하는 이메일입니다!')

# 		user = User.objects.create_user(username, email, password)
# 		user.save()
# 		user = authenticate(username=username, password=password)
# 		login(request, user)
# 		return redirect('user_profile')
# 	else:
# 		return render(request, 'accounts/user_signup.html')

# def user_login(request):
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect('user_profile')
# 		else:
# 			return render(request, 'accounts/user_login.html', {'error': '아이디나 패스워드가 올바르지 않습니다!'})
# 	else:
# 		return render(request, 'accounts/user_login.html')

# def user_logout(request):
# 	logout(request)
# 	return redirect('user_login')

# @login_required
# def user_profile(request):
# 	return render(request, 'accounts/user_profile.html', {'user': request.user})

#######################################################################################################################

# CBV(Class Based View) 방식으로 구현한 회원가입, 로그인, 로그아웃, 프로필 페이지 뷰

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/form.html",
    # success_url = settings.LOGIN_URL,
    success_url="/accounts/login/",
)

login = LoginView.as_view(
    template_name="accounts/form.html",
)

logout = LogoutView.as_view(
    # next_page = settings.LOGIN_URL,
    next_page="/accounts/login/",
)


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
