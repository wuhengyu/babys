from django.shortcuts import render, HttpResponse


# Create your views here.
def commodityView(request):
    return HttpResponse('commodityView Hello World')


def detailView(request):
    return HttpResponse('Hello World')

    # title = '商品列表'
    # classContent = 'commoditys'
