from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from commodity.models import *


# Create your views here.

def indexView(request):
    title = '首页'
    classContent = ''
    commodityInfos = CommodityInfos.objects.order_by('-sold').all()[:8]
    types = Types.objects.all()
    c1 = [x.seconds for x in types if x.first == '儿童服饰']
    clothes = CommodityInfos.objects.filter(types__in=c1).order_by('-sold')[:5]
    f1 = [x.seconds for x in types if x.first == '奶粉辅食']
    clothes = CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[:5]
    g1 = [x.seconds for x in types if x.first == '儿童用品']
    goods = CommodityInfos.objects.filter(types__in=g1).order_by('-sold')[:5]
    return render(request, 'index.html', locals())

class indexClassView(TemplateView):
