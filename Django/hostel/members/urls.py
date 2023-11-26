from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all, name='all'),
    path('add/', views.add, name='add'),
    path('get/', views.get, name='get'),
]