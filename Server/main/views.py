from django.shortcuts import render,redirect
from .serializers import listserializers
from rest_framework import viewsets
from .models import infolist
from django.http import HttpResponse

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
    return redirect('writeinfo.html')  

def showresult(request):
    resultlist = infolist.objects.all()
    return render(request,'result.html', {'resultlist' : resultlist})


class infoviewset(viewsets.ModelViewSet):
    queryset = infolist.objects.all()
    serializer_class = listserializers
