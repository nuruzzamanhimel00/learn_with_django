

from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_analysis_view, name='data_analysis_view.index'),

 
]
