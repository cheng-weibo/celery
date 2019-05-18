from django.shortcuts import render, HttpResponse
from app01.tasks import MyTask
# Create your views here.


def index(request):
    print('index')
    t = MyTask()
    t.delay(1, 2, a=3, b=4)
    return HttpResponse("OK")
