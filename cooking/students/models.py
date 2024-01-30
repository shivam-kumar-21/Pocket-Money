from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)

    def __str__(self) -> str:
        return f'{self.name} {self.phone}'
