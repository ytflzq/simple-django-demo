from __future__ import unicode_literals

from django.db import models

# Create your models here.

class School(models.Model):
    """docstring for School"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    
    class Mata:
        db_table = 'school'


class Student(models.Model):
    """docstring for Student"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,blank=True,null=True)
    age = models.IntegerField(max_length=10,blank=True,null=True)    
    height = models.IntegerField(max_length=10,blank=True,null=True)
    salary = models.DecimalField(default=0,max_digits=20,decimal_places=2)
    # school = models.ForeignKey(School)

    class Meta:
        db_table = 'student'

