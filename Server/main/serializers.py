from rest_framework import serializers
from .models import infolist

class listserializers(serializers.ListSerializer):
    class Meta:
        model = infolist
        fields = ('id','title','information','mainphoto')