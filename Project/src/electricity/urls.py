"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from landingpage import urls as landing_urls
from Register import urls as register_urls
from pricing import urls as pricing_urls
from login import urls as login_urls
from sign_up import urls as signup_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(landing_urls, namespace="landing")),
    #path("register/", include(register_urls, namespace="register")),
    path("signup/", include(signup_urls, namespace="sign_up")),
    path("pricing/", include(pricing_urls, namespace="pricing")),
    path("login/", include(login_urls, namespace="login")),
]
