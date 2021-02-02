from django.contrib import admin
from django.urls import path
import main.views
from django.conf.urls import url,include
from rest_framework import routers
from main.views import infoviewset
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('main',infoviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home),
    path('sample.php',main.views.sam)
    # path('one.html',main.views.one),
    # path('two.html',main.views.two),
    # path('three.html',main.views.three),
    # path('writeinfo.html',main.views.writeinfo),
    # path('result.html',main.views.result),
    #url(r'^writeinfo.html',include(router.urls)),
]
