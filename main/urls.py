from django.urls import include, path, reverse

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("news/", views.news, name="news"),
    path("news/<str:slug>/", views.news_article, name="article"),
    path("tour/", views.tour, name="tour"),
    path("music/", views.music, name="music"),
    path("media/", views.media, name="media"),
    path("about/", views.about, name="about"),
]
