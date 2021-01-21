"""exam URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path

from App02 import views

app_name = 'App02'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('filter/', views.fil, name='filter'),
    path('register/', views.register, name='register'),
    path('url/', views.include_url, name='url'),
    path('data/', views.handle_data, name='data'),
    path('search/', views.search, name='search'),
    path('send/', views.send, name='send'),
    path('page/', views.show_page, name='page'),
    path('page/<int:page_num>', views.show_page, name='page'),
    path('login/',views.login,name='login'),

]
