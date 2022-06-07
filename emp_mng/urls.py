from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('add_emp', views.add_emp , name='add_emp'),
    path('del_emp', views.del_emp , name='del_emp'),
    path('del_emp/<int:emp_id>', views.del_emp , name='del_emp'),
    path('view_emp', views.view_emp , name='view_emp'),
    path('fil_emp', views.fil_emp , name='fil_emp'),
]