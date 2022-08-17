from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def shopperView(request):
    return HttpResponse('Hello World')


def loginView(request):
    return HttpResponse('Hello World')


def logoutView(request):
    return HttpResponse('Hello World')


def shopcart(request):
    return HttpResponse('Hello World')
