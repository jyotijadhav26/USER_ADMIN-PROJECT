from django.db import models

# Create your models here.
class Faculty(models.Model):
    FName=models.CharField(max_length=20)
    FEdu=models.CharField(max_length=20)
    FImage = models.ImageField(upload_to='faculty_images/')    
    