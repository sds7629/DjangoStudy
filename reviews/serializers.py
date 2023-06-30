from rest_framework.serializers import ModelSerializer
from .models import Review


class BoardReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ("writer", "content")
class BoardReviewDetailSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"