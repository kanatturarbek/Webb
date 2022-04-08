from distutils.file_util import move_file
from itertools import count
from xmlrpc.client import Boolean
from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.FloatField(default=0)
    description=models.TimeField
    count=models.IntegerField
    is_active=models.BooleanField


class Category(models.Model):
    name=models.CharField