from django.shortcuts import render,redirect
from .serializers import listserializers
from rest_framework import viewsets
from .models import infolist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.template.defaultfilters import register
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request,'home.html')

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,'two.html')

def three(request):
    return render(request,'three.html')

def writeinfo(request):
    return render(request,'writeinfo.html')

def result(request):
    return render(request,'result.html')

def saveinfo(request):
    if(request.method == 'POST'):
      post = infolist()
      post.title = request.POST['title']
      post.information = request.POST['information']
      post.save()
    return redirect('http://localhost:8000/')  

def showresult(request):
    resultlist = infolist.objects.all()
    return render(request,'result.html', {'resultlist' : resultlist})

@method_decorator(csrf_exempt,name='dispatch')
def showdetail(request):
    if request.method == "GET":
        return render(request,'infodetail.html')
    elif request.method == "POST":
        code = request.POST.get('id')
        recode = code[:-1]
        detail = infolist.objects.get(id = recode)
        # detail = infolist.objects.get(information = request)
        return render(request,'infodetail.html',{'detail':detail})        

def logout(request):
    print("함수가 실행되었습니다.")
    auth.logout(request)
    return redirect('http://localhost:8000/')       

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('http://localhost:8000/')
        else :
            return render(request, 'login.html', {'error' : '아이디 또는 비밀번호가 옳지 않습니다. ㅜㅜ'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method =="POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password1"])
            auth.login(request, user)
            return redirect('http://localhost:8000/')
    return render(request,'signup.html')


class infoviewset(viewsets.ModelViewSet):
    queryset = infolist.objects.all()
    serializer_class = listserializers
