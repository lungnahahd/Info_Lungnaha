from django.contrib import admin

from .models import infolist
from .forms import infopost
from django import forms
from django.db import models
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField





# #information = RichTextUploadingField()
# class PostAdminForm(forms.ModelForm):
#     #title = forms.CharField(widget=CKEditorUploadingWidget)
#     #inforamtion = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = infolist
#         fields = "__all__"

# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm

# admin.site.register(infolist, PostAdmin)