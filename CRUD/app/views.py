from django.shortcuts import render
from .models import Student
from .serialize import studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django import forms
# Create your views Data Here.

def adddata(request):
    if request.method == 'POST':
        studentid = request.POST['id']
        studentname = request.POST['name']
        studentnickname = request.POST['nickname']

        alldata = Student(StudentId = studentid,StudnetName = studentname,StudnetNickName = studentnickname)
    context = {'alldata' : alldata}
    return render(request,'adddata.html',context)

def showdata(request):
    stu = Student.objects.all()
    serializer = studentserializer(stu,many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')


def update_data(request,pk):
    stu = Student.objects.get(id=pk)    
    serializer = studentserializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')


def deletedata(request):
    pass