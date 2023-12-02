from django.db import models

#create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    addr=models.CharField(max_length=100)
