from rest_framework.serializers import ModelSerializer
from .models import Board
# from users.models import User
from users.serializers import UserSerializer
from reviews.serializers import BoardReviewSerializer




class BoardSerializer(ModelSerializer):
    user = UserSerializer(read_only = True)
    review_set = BoardReviewSerializer(many = True, read_only = True)

    class Meta:
        model = Board
        fields = "__all__"
        


# 전체 리뷰를 보여주는 API
# 특정 ID 값 리뷰를 보여주는 API