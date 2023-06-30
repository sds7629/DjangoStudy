from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllUsers.as_view()),
    path("myinfo/<int:user_id>", views.UserInfo.as_view())
]