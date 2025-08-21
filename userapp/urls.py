
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.emp_info,name='display'),
    path('add/',views.add_emp,name='addemp'),
    path('update/<int:id>', views.update_emp,name='update'),
    path('delete/<int:id>',views.delete_emp,name='delete')
    
]