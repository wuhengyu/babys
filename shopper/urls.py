# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 19:41
# @Author  : Walter
# @File    : urls.py
# @License : (C)Copyright Walter
# @Desc    :
from django.urls import path
from .views import *

urlpatterns = [
    path('.html', shopperView, name='shopper'),
    path('login.html', loginView, name='login'),
    path('logout.html', logoutView, name='logout'),
    path('shopcart.html', shopcartView, name='shopcart'),
]