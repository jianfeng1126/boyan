from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .models import Users
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect


# def tologin(request):
#     return render(request, 'login.html')

def login(request):
    username = request.POST.get("username");
    userpassward = request.POST.get("userpassward");
    user=Users.objects.filter(username=username, userpassward=userpassward)
    if user:
        return redirect('/dept/listdazhong/')
    else:
        return render(request,'login.html',{"MESSAGE":"用户名和密码错误"})


def index(request):
    return render(request,'list2.html')

# def toadd(request):
#     return render(request,'useradd.html')
#
# def useradd(request):
#     username = request.POST.get("username")
#     userpassward = request.POST.get("userpassward")
#     Users(username=username, userpassward=userpassward).save()
#     return login(request)

