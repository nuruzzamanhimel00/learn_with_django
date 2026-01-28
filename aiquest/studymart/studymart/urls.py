"""
URL configuration for studymart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
