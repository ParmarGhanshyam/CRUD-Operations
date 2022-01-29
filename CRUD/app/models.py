from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId = models.IntegerField()
    StudnetName  = models.CharField(max_length=50)
    StudnetNickName = models.CharField(max_length=50)

    def __str__(self):
        self.StudentId
    