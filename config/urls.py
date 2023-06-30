"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 127.0.0.1:8000/api/v1/users

    path('api/v1/board/', include("boards.urls")),
    path('api/v1/reviews/', include("reviews.urls")),
    path('api/v1/users/', include("users.urls")),
    # path('api/v1/users/', include("users.urls")),

    #업데이트를 하는 경우 이전 버전 사용자도 로그인이 되어야 하기 때문에 버전을 나눈다.
    # path('api/v2/board', include("boards.urls"))
    # path('board/', views.show_board),
    # path('board/all', views.all_board),
]
