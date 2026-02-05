
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect



urlpatterns = [
    # path('', lambda request: redirect('machine_learning/', permanent=False)),
    path('', include('Home_page.urls')),
    path('about_us/', include('About_us.urls')),
    path('data_analysis/', include('Data_Analysis.urls')),
    path('deep_learning/', include('Deep_learning.urls')),
    path('machine_learning/', include('machine_learning.urls')),
   
]
