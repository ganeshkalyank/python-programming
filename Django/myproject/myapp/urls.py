from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("edit/<int:task_id>", views.edit, name="edit"),
    path("delete/<int:task_id>", views.delete, name="delete"),
]
