from multiprocessing import context
from operator import index
from unicodedata import name
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from emp_mng.models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'index.html')



def del_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_rev = Employee.objects.get(id = emp_id)
            emp_rev.delete()
            HttpResponse("remove successfully")
        except:
            HttpResponse("enter the valid emp_id")
        


    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'del_emp.html', context)

def fil_emp(request):
    if request.method=="POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(Last_name__icontains = name))

        if dept:
            emps = emps.filter(dept__name__icontains = dept)

        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps' : emps
        }

        return render(request, 'view_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'fil_emp.html')

    else:
        HttpResponse("Invalid request")

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'view_emp.html' , context)


def add_emp(request):
    if request.method == "POST":
        first_name  = request.POST['first_name']
        Last_name  = request.POST['Last_name']
        dept  = int(request.POST['dept'])
        salary  = int(request.POST['salary'])
        phone  = int(request.POST['phone'])
        role  = int(request.POST['role'])
        bonus  = int(request.POST['bonus'])

        add_emp = Employee(first_name=first_name , Last_name=Last_name, dept_id=dept, salary=salary, bonus=bonus, phone=phone, role_id=role)

        add_emp.save()


    return render(request, 'add_emp.html')        

