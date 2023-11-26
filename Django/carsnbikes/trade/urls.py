from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sell/', views.sell),
    path('buy/', views.buy),
]