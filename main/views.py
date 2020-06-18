from django import http
from django.shortcuts import render
from django.utils import timezone

from . import models


def index(request):
    current_date = timezone.localtime().date()
    news = models.News.objects.filter(published__lte=current_date).order_by(
        "-published"
    )[:3]
    events = models.Event.objects.all().order_by("-date")[:3]
    if request.is_ajax():
        form = forms.LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponse(status=200)
        return http.HttpResponse(status=400)
    return render(request, "main/index.html", {"news": news, "events": events})


def news(request):
    current_date = timezone.localtime().date()
    news = models.News.objects.filter(published__lte=current_date).order_by(
        "-published"
    )
    return render(request, "main/news.html", {"news": news})


def news_article(request, slug):
    article = models.News.objects.get(slug=slug)
    return render(request, "main/news-article.html", {"article": article})


def tour(request):
    events = models.Event.objects.all().order_by("-date")
    return render(request, "main/tour.html", {"events": events})


def music(request):
    music = models.Music.objects.all()
    return render(request, "main/music.html", {"music": music})


def media(request):
    media = models.Media.objects.all()
    return render(request, "main/media.html", {"media": media})


def about(request):
    return render(request, "main/about.html", {})
