from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Thing(models.Model):
	name = models.TextField(UNIQUE=True,blank =False,max_length=30)
	description = models.TextField(UNIQUE=False,blank =True,max_length=120)
	quantity = models.IntegerField(UNIQUE=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
