from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class infolist (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    information = RichTextUploadingField()

    def __str__(self):
        return self.title    
