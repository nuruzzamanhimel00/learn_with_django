
from django.urls import path
from . import views

urlpatterns = [
    path('', views.deep_learning_view, name='deep_learning_view'),

 
]
