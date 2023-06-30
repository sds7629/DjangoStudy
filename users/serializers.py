from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name","gender", "age")

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"