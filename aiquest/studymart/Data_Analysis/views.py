from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_analysis_view(request):
    return render(request, 'Data_Analysis/index.html')