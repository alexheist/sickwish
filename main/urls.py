from django.urls import include, path, reverse
from . import views

urlpatterns = [
    path("", views.index),
    path("news/", views.news),
    path("news/<str:slug>/", views.news_article),
    path("tour/", views.tour),
    path("music/", views.music),
    path("media/", views.media),
    path("about/", views.about),
]
