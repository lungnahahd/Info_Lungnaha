from django.contrib import admin

from .models import infolist
from django import forms
from ckeditor.widgets import CKEditorWidget


class EventAdminForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    information = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = infolist

class EventAdmin(admin.ModelAdmin):
    form  =EventAdminForm



admin.site.register(infolist, EventAdmin)

