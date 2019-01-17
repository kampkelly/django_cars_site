from django.db import models

# Create your models here.
class Car(models.Model):
    colour = models.CharField(max_length=200,default='black')
    model = models.CharField(max_length=200,null=False)
    name = models.CharField(max_length=200,unique=True,null=False)
    year = models.IntegerField(null=False)


class User(models.Model):
    name = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=200,null=False)
    password = models.CharField(max_length=255,null=False)