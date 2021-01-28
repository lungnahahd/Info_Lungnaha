from django.shortcuts import render
from .serializers import listserializers
from rest_framework import viewsets
from .models import infolist

def home(request):
    return render(request,'home.html')

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,'two.html')

def three(request):
    return render(request,'three.html')


class infoviewset(viewsets.infoviewset):
    queryset = infolist.objectes.all()
    serializer_class = listserializers
