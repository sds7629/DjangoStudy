from django.db import models
from django.utils import timezone
from common.models import CommonModel

class Story(models.Model):
    writer = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = "")
    time = models.DateTimeField(timezone.now())
    likes = models.PositiveIntegerField()
    views = models.PositiveIntegerField()
    views_people = models.CharField(max_length = 100)
# Create your models here.
