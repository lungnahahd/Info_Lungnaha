from django.contrib import admin
from django.urls import path
import main.views
from django.conf.urls import url,include
from rest_framework import routers
from main.views import infoviewset

router = routers.DefaultRouter()
router.register('main',infoviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home),
    path('one.html',main.views.one),
    path('two.html',main.views.two),
    path('three.html',main.views.three),
    path('writeinfo.html',main.views.writeinfo),
    #url(r'^writeinfo.html',include(router.urls)),
]
