from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-writer/", views.create_writer, name="create-writer"),
    path("create-post/", views.create_post, name="create-post"),
]
