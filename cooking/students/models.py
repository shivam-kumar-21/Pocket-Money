from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length= 20)
