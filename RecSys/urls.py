# RecSys/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend, name='recommend'),  # Ensure this line is correct
]
