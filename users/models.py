from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length = 150, editable=False)
    last_name = models.CharField(max_length = 150, editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField()
    age = models.PositiveIntegerField(default = 0)
    gender = models.CharField(max_length=10)

    is_business = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.name} / {self.age}"
# Create your models here.
