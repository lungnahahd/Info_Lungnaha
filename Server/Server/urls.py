from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home),
    path('one.html',main.views.one),
    path('two.html',main.views.two),
    path('three.html',main.views.three),
]
