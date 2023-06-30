from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response # 클라이언트로 데이터를 내려주는 부분 
from rest_framework.exceptions import NotFound
from .models import Review
from .serializers import BoardReviewSerializer,BoardReviewDetailSerializer

# Create your views here.
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all() # 장고 객체
        serializer = BoardReviewSerializer(reviews, many=True) #장고 객체를 JSON으로 변환
        return Response(serializer.data)
    
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id = review_id)
        except:
            raise NotFound
        serializer = BoardReviewDetailSerializer(review)
        return Response(serializer.data)
