"""centproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.views.decorators.csrf import  csrf_exempt

import xadmin

from apps.users.views import LoginView, LogoutView, SendSmsView, DynamicLoginView, CreateQRcodeView, QrLoginView,VoiceLoginView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),

    path('login/', LoginView.as_view(), name="login"),
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    path('qr_login/', QrLoginView.as_view(), name="qr_login"),
    path('voice_login/', VoiceLoginView.as_view(), name="voice_login"),

    
    path('logout/', LogoutView.as_view(), name="logout"),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),
    url(r'^create_qrcode/', csrf_exempt(CreateQRcodeView.as_view()), name="create_qrcode"),
]
