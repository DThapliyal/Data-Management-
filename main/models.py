from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    City=models.CharField(max_length=20)
    Department=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)

