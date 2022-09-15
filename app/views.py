from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
#  def index(request):

#     return HttpResponse("<h1>Hello World</h1>")

def Shireen(request):
    return HttpResponse("<h1>Hey, this is Shireen.</h1>")

def ShireenPsid(request):
    return HttpResponse("<h1>My PSID id 50411.</h1>")

def index(request):
    Students=Student.objects.all().values("firstname","lastname","dateenrolled","estatus","contactnum","course__cname","course__cid")
    return render(request,"index.html",{"Students":Students})

def search(request):
    return render(request,"search.html")

def search_action(request):
    search_item=request.GET.get("search_item")
    Students=list(Student.objects.filter(firstname__icontains=search_item).values("firstname","lastname","dateenrolled","estatus","contactnum","course__cname","course__cid"))
    return JsonResponse({"filtered_response":Students})

def signup(request):
    return render(request,"signup.html")

def signup_action(request):
    username=request.POST.get("email")
    password=request.POST.get("password")
    name=request.POST.get("name")
    user=User.objects.create_user(username=username,password=password,first_name=name)
    auth.login(request,user=user)
    return redirect('index')

def signin(request):
    return render(request,"signin.html")

def signin_action(request):
    username=request.POST.get("email")
    password=request.POST.get("password")
    user=auth.authenticate(request,username=username,password=password)
    auth.login(request,user=user)
    return redirect('index')


def courseid(request):
    Students=Student.objects.all().values("course__cid")
    return render(request,"courseid.html",{"Students":Students})