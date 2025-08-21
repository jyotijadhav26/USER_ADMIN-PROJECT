from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_No=models.IntegerField()
    Emp_Name=models.CharField(max_length=20)
    Location=models.CharField(max_length=20)
    
    
    
