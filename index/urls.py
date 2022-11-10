# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 19:41
# @Author  : Walter
# @File    : urls.py
# @License : (C)Copyright Walter
# @Desc    :
from django.urls import path
from .views import *

urlpatterns = [
    path('', indexClassView.as_view(), name='index'),
    path('index1', index1, name='index1')
]