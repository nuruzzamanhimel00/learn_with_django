from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def deep_learning_view(request):
    return HttpResponse("This is the Deep Learning view.")

def about_view(request):
    return HttpResponse("This is the About view.")