from .models import Student
from rest_framework import serializers 

class studentserializer(serializers.Serializer):
    StudentId = serializers.IntegerField()
    StudnetName = serializers.CharField(max_length = 30)
    StudnetNickName = serializers.CharField(max_length = 30)


    