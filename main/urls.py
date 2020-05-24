from django.urls import include, path, reverse
from . import views

urlpatterns = [
    path("", views.index),
]
