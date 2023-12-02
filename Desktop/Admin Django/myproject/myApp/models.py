from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin=models.BooleanField("is admin",default=False)
    is_employee=models.BooleanField("is employee",default=False)
    is_customer=models.BooleanField("is customer",default=False)
    is_student=models.BooleanField("is student",default=False)