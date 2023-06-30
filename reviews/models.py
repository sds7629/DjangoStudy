from django.db import models
from django.utils import timezone


class Review(models.Model):
    writer = models.CharField(max_length=60)
    date = models.DateTimeField(timezone.now())
    likes = models.PositiveIntegerField()
    content = models.TextField()
    board = models.ForeignKey("boards.Board",on_delete=models.CASCADE)
    user = models.ForeignKey("users.User",on_delete=models.CASCADE)
    
# Create your models here.
