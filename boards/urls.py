from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.show_board),
#     path("all/", views.all_board),
#     path("<int:board_id>/<str:board_content>/", views.make_board),
#     path("all_boards/", views.show_all_board),
#     path("board_reviews/<int:board_id>", views.show_board_reviews),
# ]

urlpatterns = [
    path("", views.Boards.as_view()),
    path("<int:board_id>/", views.BoardDetail.as_view()),
]