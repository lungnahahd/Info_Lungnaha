from django.db import models

class infolist (models.Model):
    title = models.CharField(max_length=30)
    information = models.CharField(max_length=500)
    now = models.DateTimeField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
