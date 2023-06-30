from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response # 클라이언트로 데이터를 내려주는 부분 
from rest_framework.exceptions import NotFound
from .serializers import UserInfoSerializer, UserSerializer


class AllUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
# Create your views here.

class UserInfo(APIView):
    def get(self, request, user_id):
        try:
            users = User.objects.get(id=user_id)
        except:
            raise NotFound
        serializer = UserInfoSerializer(users)
        return Response(serializer.data)
        
