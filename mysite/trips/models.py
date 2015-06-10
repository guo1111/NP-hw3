from django.db import models

# Create your models here.
class Data(models.Model):
	name = models.CharField(max_length=100)
	sex = models.CharField(max_length=100)
	height = models.CharField(max_length=100)
	weight = models.CharField(max_length=100)
	hobby = models.CharField(max_length=100)
	time = models.CharField(max_length=100)
	

class Account(models.Model):
	name = models.CharField(max_length=100)
	pwd = models.CharField(max_length=100)