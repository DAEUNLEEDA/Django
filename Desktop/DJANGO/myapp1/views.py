from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome!')
#index 함수 첫번째 파라미터 : request
#HttpResponse라는 것 import