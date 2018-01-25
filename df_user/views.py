from django.shortcuts import render,redirect
from df_user.models import Passport
# Create your views here.
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    # 1.获取用户注册信息
    username=request.POST.get('user_name')
    password =request.POST.get('pwd')
    email =request.POST.get('email')
    # 2.将用户信息存入数据库
    # passport=Passport(username=username,password=password,email=email)
    # # passport.username=username
    # # passport.password=password
    # # passport.email=email
    # passport.save()
    Passport.objects.add_one_passport(username=username,password=password,email=email)
    # 3。跳转到登录页面
    return redirect('/user/login/')

def index(request):
    return HttpResponse('hello word')

