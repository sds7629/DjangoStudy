from django.db import models

class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True) # auto_now_add = 객체가 생성되는 시간을 기준
    updated = models.DateTimeField(auto_now=True) # auto_now = 객체가 업데이트되는 시간을 기준
# Create your models here.
    #위 모델을 추상화 하겠다. = Meta(모델로 사용하는 것이 아니라 다른 객체(모델)에서 활용이 가능하게끔 한다.)
    class Meta:
        abstract = True