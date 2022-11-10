from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from commodity.models import *

# locals() 函数会以字典类型返回当前位置的全部局部变量
# def indexView(request):
#     title = '首页'
#     classContent = ''
#     commodityInfos = CommodityInfos.objects.order_by('-sold').all()[:8]
#     types = Types.objects.all()
#     c1 = [x.seconds for x in types if x.first == '儿童服饰']
#     clothes = CommodityInfos.objects.filter(types__in=c1).order_by('-sold')[:5]
#     f1 = [x.seconds for x in types if x.first == '奶粉辅食']
#     clothes = CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[:5]
#     g1 = [x.seconds for x in types if x.first == '儿童用品']
#     goods = CommodityInfos.objects.filter(types__in=g1).order_by('-sold')[:5]
#     return render(request, 'index.html', locals())

class indexClassView(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {'title': '首页', 'classContent': ''}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commodityInfos'] = CommodityInfos.objects.order_by('-sold').all()[:8]
        types = Types.objects.all()
        c1 = [x.seconds for x in types if x.first == '儿童服饰']
        clothes = CommodityInfos.objects.filter(types__in=c1).order_by('-sold')[:5]
        f1 = [x.seconds for x in types if x.first == '奶粉辅食']
        clothes = CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[:5]
        g1 = [x.seconds for x in types if x.first == '儿童用品']
        goods = CommodityInfos.objects.filter(types__in=g1).order_by('-sold')[:5]
        return context


    def get(self, request, *args, **kwargs):
        pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


    def post(self, request, *args, **kwargs):
        pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)



def index1(request):
    return render(request, 'index1.html', locals())