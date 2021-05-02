from django.db import models
# from django.core.exceptions import FieldDoesNotExist
# Create your models here.


class Courses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    date = models.DateField()
    branch = models.CharField(max_length=50,default=None)
    credit = models.CharField(max_length=2,default=None)
    dis = models.CharField(max_length=800,default=None)
    fac1 = models.CharField(max_length=10,default=None)
    fac2 = models.CharField(max_length=10,default=None)
    fac3 = models.CharField(max_length=10,default=None)
    ttime = models.FloatField()
    ctype = models.BooleanField(default=False)