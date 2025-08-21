from django.shortcuts import render

# Create your views here.

from userapp.models import Employee
from .models import Faculty
from django.conf import settings

def showemp(request):
    s = Employee.objects.all()
    F = Faculty.objects.all()
    return render(request, 'showemp.html', {'s': s, 'F': F, 'MEDIA_URL': settings.MEDIA_URL})
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_faculty(request):

    if request.method =="POST":
        fname=request.POST.get('fname')
        fedu=request.POST.get('fedu')
        fimg=request.FILES.get('fimg')
        Faculty.objects.create(FName=fname,FEdu=fedu,FImage=fimg)
        F=Faculty.objects.all()        
        return render(request,'showemp.html',{'F':F})
        
    return render(request,'faculty.html')

