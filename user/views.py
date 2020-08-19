from django.shortcuts import render,HttpResponse
# Create your views here.
def login(request):
    # return HttpResponse('<h1>登录成功</h1>')
    return render(request, 'static/login_app/html/login.html')
def register(request):
    return render(request, 'static/login_app/html/register.html')
def demo1(request):
    return render(request, 'static/login_app/html/test.html')