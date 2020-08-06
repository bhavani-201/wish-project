from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld_view(request):
    msg='<h1>Hello World How Are You</h1>'
    return HttpResponse(msg)

def second_view(request):
    msg='<h1>Hello SecondView</h1>'
    return HttpResponse(msg)

def third_view(request):
    msg='<h1>Hello thirdview</h1>'
    return HttpResponse(msg)
