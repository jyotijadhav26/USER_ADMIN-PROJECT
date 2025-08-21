from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.showemp,name='showemp'),
    path('add/',views.add_faculty,name='addfaculty')
  
    
]
