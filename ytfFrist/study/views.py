from django.shortcuts import render
from django.http import HttpResponse
from study.models import *
import json
import datetime
# Create your views here.
def hello(response):

    return HttpResponse("hello,")
#add student
def add_stu(request):
    name  = request.POST.get("name","")
    age  = request.POST.get("age",0)
    height  = request.POST.get("height",0)
    salary  = request.POST.get("salary",0)
    try:
        add_stu = Student(name=name,age=age,height=height,salary=salary)
        add_stu.save()
    except Exception, e:
        return HttpResponse({'fail':'fail'})
    return HttpResponse({'success':'success'})
#show all student
def show_stu(request):
    stu_info = Student.objects.all()
    cur_time = datetime.datetime.now()
    return render(request,'index.html',{'info':stu_info,'cur_time':cur_time})
    pass

#delete student by id
def del_stu(request):
    stu_id = request.GET.get('id')
    try:
        Student.objects.filter(id=stu_id).delete()
    except Exception, e:
        return HttpResponse({'status':'fail','mes':' delete fail'})
    return HttpResponse({'status':'success','mes':' delete success'})

#update student
def update_stu(request):
    stu_id = request.POST.get('id')
    name  = request.POST.get("name","")
    age  = request.POST.get("age",0)
    height  = request.POST.get("height",0)
    salary  = request.POST.get("salary",0)
    try:
        Student.objects.filter(id=stu_id).update(name=name,age=age,height=height,salary=salary)
    except Exception, e:
        return HttpResponse({'status':'fail','mes':' update fail'})
    return HttpResponse({'status':'success','mes':' update success'})
