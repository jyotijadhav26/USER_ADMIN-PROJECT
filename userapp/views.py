from django.shortcuts import render

# Create your views here.
from .models import Employee
def emp_info(request):
    s=Employee.objects.all()
    
    
    return render(request,'display.html',{'s':s})

def add_emp(request):
    if request.method=="POST":
        Emp_No=request.POST.get('em_no')
        Emp_Name=request.POST.get('em_name')
        Location=request.POST.get('location')
        Employee.objects.create(Emp_No=Emp_No,Emp_Name=Emp_Name,Location=Location)
        s=Employee.objects.all()
        return render(request,'display.html',{'s':s})
         
    
    return render(request,'addemp.html')


def update_emp(request,id):
    u=Employee.objects.get(id=id)
    if request.method=="POST":
        u.Emp_No=request.POST.get('em_no')
        u.Emp_Name=request.POST.get('em_name')
        u.Location=request.POST.get('location')
        u.save()
        s=Employee.objects.all()
        return render(request,'display.html',{'s':s})
    
    return render(request,'update_emp.html',{'u':u})


def delete_emp(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    s=Employee.objects.all()
    return render(request,'display.html',{'s':s})