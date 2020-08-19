from django.shortcuts import render

# Create your views here.
def home(request):
    return None


# -*- coding: utf-8 -*-

from django.http import HttpResponse

from home.models import Test
# 数据库操作
def homedb(request):
    data_value = Test.objects.all()
    data = {'data_name':data_value}
    print(dict(data))
    # test1 = Test(name='mydatabase')
    # test1.save()
    return render(request,'../templates/static/home_page/html/home.html',context=data)