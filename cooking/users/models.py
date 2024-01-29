from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    )

    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='student')

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length= 20)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'