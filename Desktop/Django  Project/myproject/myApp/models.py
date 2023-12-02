from django.db import models
from django.db.models import F, Func


import math

from django.db.models.expressions import Func
from django.db.models.fields import FloatField, IntegerField
from django.db.models.functions import Cast
from django.db.models.functions.mixins import (
    FixDecimalInputMixin, NumericOutputFieldMixin,
)
from django.db.models.lookups import Transform


# Create your models here.
class Employee(models.Model):
    value1=models.CharField(max_length=100)
    selectopr=models.CharField(max_length=100)
    value2=models.CharField(max_length=100)

class Sin(NumericOutputFieldMixin, Transform):
    function = 'SIN'
    lookup_name = 'sin'

