from django.db import models
from django.utils import timezone


class Chatting(models.Model):
    receiver_id = models.CharField(max_length = 50)
    content = models.TextField()
    reply = models.TextField()
    is_view = models.CharField(max_length = 50)
    is_view_num = models.PositiveIntegerField()
    send_time = models.DateTimeField(timezone.now())

# Create your models here.
