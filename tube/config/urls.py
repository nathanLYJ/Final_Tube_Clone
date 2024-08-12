from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from tube import views

urlpatterns = [
    path("admin/", admin.site.urls),  # 관리자 페이지 URL
    path("tube/", include("tube.urls")),  # tube 앱의 URL 패턴 포함
    path("accounts/", include("accounts.urls")),  # accounts 앱의 URL 패턴 포함
    path("", views.tube_list, name="tube_list"),]

# 미디어 파일 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
