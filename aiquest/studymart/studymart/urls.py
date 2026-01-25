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
from django.urls import path
# from machine_learning import views as mlv
from machine_learning.views import index as index_view,  deep_learning_view, about_view
from About_us import views as auv
from Data_Analysis import views as dav
from Deep_learning import views as dlv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('deep-learning/', deep_learning_view, name='deep_learning'),
    path('about/', about_view, name='about'),
    path('about-us/', auv.about_us, name='about_us'),
    path('data-analysis/', dav.data_analysis_view, name='data_analysis'),
    path('deep-learning-view/', dlv.deep_learning_view, name='deep_learning_view'),
]
