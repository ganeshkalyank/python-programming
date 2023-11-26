from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('insert/', views.insert),
    path('all/', views.all),
    path('edit/<int:plant_id>/', views.edit),
]
