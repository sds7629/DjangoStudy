# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Board
# from reviews.models import Review

# def show_board(request):
#     return HttpResponse("show board")

# def all_board(request):
#     # boards = Board.objects.all()
#     return HttpResponse("All board")

# def make_board(request,board_id,board_content):
#     return HttpResponse(f"Make board / id:{board_id} / content:{board_content}")

# #Rendering

# def show_all_board(request):
#     boards = Board.objects.all()
#     return render(request, "all_boards.html", {"datas": boards, "status": "success"})


# def show_board_reviews(request, board_id):
#     boards = Board.objects.get(id = board_id)
#     return render(request, "reviews.html", {"datas": boards})



####################################################

# views.py
# 클라이언트에서 받은 데이터를 처리해주는 부분
# HTTP METHOD
from rest_framework.views import APIView
from rest_framework.response import Response # 클라이언트로 데이터를 내려주는 부분 
from rest_framework.exceptions import NotFound, NotAuthenticated # 데이터를 찾지 못한 경우에 내려주는 오류
from rest_framework.status import HTTP_204_NO_CONTENT
from .serializers import BoardSerializer
from .models import Board


# GET: 전체 게시글 불러오기
# POST: 게시글 작성하기(Create)
class Boards(APIView):
    def get(self, request):
        boards = Board.objects.all() # 타입은 QuerySet  React가 이해하지 못함
        # 장고 객체 -> json(Serializer)
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # JSON -> 장고 객체(역직렬화)
        serializer = BoardSerializer(data=request.data) # JSON -> OBJECTS
        
        if request.user.is_authenticated:
            if serializer.is_valid():
                board = serializer.save(user = request.user) # 데이터 저장
                serializer = BoardSerializer(board)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated
        
# GET: 유저로부터 입력받은 id 값의 게시글 데이터 불러오기
class BoardDetail(APIView):
    def get(self, request, board_id):
        # request: React에서 데이터를 담아서 보내준 부분
        # board_id: URL을 통해서 데이터를 전달받는 부분
        try:
            boards = Board.objects.get(id = board_id)
            # 장고객체 -> JSON (Serializer)
        except Board.DoesNotExist:
            raise NotFound
        serializer = BoardSerializer(boards)
        print(serializer)
        return Response(serializer.data)

# api/v1/boards/<int:id> => DELETE // BoardDetail
    def delete(self, request, board_id):
        board = Board.objects.get(id = board_id)

        # if request.user.is_authenticated:
        #     raise NotAuthenticated
        
        if request.user != board.user:
            raise PermissionError
        
        board.delete()

        return Response(status = HTTP_204_NO_CONTENT)

    def put(self, request, board_id):
        board = Board.objects.get(id = board_id)
        if request.user != board.user:
            raise PermissionError
        
        serializer = BoardSerializer(
            board,
            data = request.data,
            context = {"request":request},
            partial = True,
        )

        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)