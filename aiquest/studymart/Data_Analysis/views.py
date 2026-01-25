from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_analysis_view(request):
    return HttpResponse("This is the Data Analysis page of StudyMart.")