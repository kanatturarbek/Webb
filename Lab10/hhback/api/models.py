from distutils.file_util import move_file
from itertools import count
from unicodedata import category
from unittest.util import _MAX_LENGTH
from xmlrpc.client import Boolean
from django.db import models





class Company(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=300,default='none')
    city=models.CharField(max_length=300)
    address=models.TextField(max_length=300,default='none')
    def to_js(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }


class Vacancy(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=300,default='none')
    salary=models.FloatField(default=0)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
       
    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'salary':self.salary
            # 'company':self.company
        }