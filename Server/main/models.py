from django.db import models

class infolist (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=30)
    information = models.CharField(max_length=500)
    id = models.AutoField(primary_key=True)
    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
