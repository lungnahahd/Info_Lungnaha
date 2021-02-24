from django.contrib import admin
from django.urls import path
import main.views
from django.conf.urls import url,include
from rest_framework import routers
from main.views import infoviewset
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache

router = routers.DefaultRouter()
router.register('main',infoviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home),
    path('one.html',main.views.one),
    path('two.html',main.views.two),
    path('three.html',main.views.three),
    path('writeinfo.html',main.views.writeinfo),
    path('saveinfo',main.views.saveinfo,name='saveinfo'),
    path('result.html',main.views.showresult),
    path('infodetail.html',main.views.showdetail),
    path('login.html/',main.views.login,name='login'),
    path('signup.html/',main.views.signup,name='signup'),
    path('logout.html/',main.views.logout,name='logout'),
    path('deleteinfo',main.views.deleteinfo,name='deleteinfo'),
    path('changedata',main.views.changedata, name='changedata'),
    path('update',main.views.update, name='update'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('index.html/', main.views.sample),

]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
