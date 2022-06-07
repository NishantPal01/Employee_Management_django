from pyexpat import model
from winreg import DeleteKey
from django.db import models
from django.forms import DateField

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100 , null=False)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100 , null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    Last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role = models.ForeignKey(Role , on_delete=models.CASCADE)
    

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.Last_name, self.phone)
