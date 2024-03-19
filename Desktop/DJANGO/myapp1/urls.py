
from django.urls import path
from myapp1 import views #import 해주기

urlpatterns = [
    path('', views.index),
    path('create/'),
    path('read/1/')
]

#admin이 아닌 다른 경로로 접속하면 myapp으로 가게 됨 (home, create, read)
#여기서 view로 이동하려면 view 설정 (함수 등)

#