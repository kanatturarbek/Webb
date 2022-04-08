from distutils.file_util import move_file
from itertools import count
from unicodedata import category
from unittest.util import _MAX_LENGTH
from xmlrpc.client import Boolean
from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.FloatField(default=0)
    description=models.TextField(max_length=300,default='none')
    count=models.IntegerField(default=0)
    is_active=models.BooleanField(default=False)
    category_id=models.IntegerField(default=0)


    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active
        }

class Category(models.Model):
    name=models.CharField(max_length=300)
    

    def to_js(self):
        return{
            'id':self.id,
            'name':self.name
        }
