from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'hello.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")