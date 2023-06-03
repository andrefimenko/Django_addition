"""Defines the route for addition."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.addition, name='addition'),
]
