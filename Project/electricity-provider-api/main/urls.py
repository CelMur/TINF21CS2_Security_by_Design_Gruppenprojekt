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

from authentication import urls as authentication_urls
from registration import urls as registration_urls
from address import urls as address_urls
from contract import urls as contract_urls
from energy_tariff import urls as energy_tariff_urls
from ui_main_page import urls as ui_main_page_urls
from ui_login_page import urls as ui_login_page_urls
from ui_register_page import urls as ui_register_page_urls
from ui_customer_page import urls as ui_customer_page_urls
from ui_customer_profile_page import urls as ui_customer_profile_page_urls
from ui_contract_page import urls as ui_contract_page_urls

#TODO: add base path api/v1/
urlpatterns = [
    path('api/v1/auth/', include(authentication_urls)),
    path('api/v1/register/', include(registration_urls)),
    path('api/v1/adress/', include(address_urls)),
    path('api/v1/contract/', include(contract_urls)),
    path('api/v1/tariff/', include(energy_tariff_urls)),
    path('', include(ui_main_page_urls)),
    path('login/', include(ui_login_page_urls)),
    path('register/', include(ui_register_page_urls)),
    path('customer/', include(ui_customer_page_urls)),
    path('profile/', include(ui_customer_profile_page_urls)),
    path('contract/', include(ui_contract_page_urls))
]
