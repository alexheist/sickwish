from django import http
from django.shortcuts import render
from django.utils import timezone

from . import models, forms


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def index(request):
    banner = get_or_none(models.Banner, in_use=True)
    current_date = timezone.localtime().date()
    news = models.News.objects.filter(published__lte=current_date).order_by(
        "-published"
    )[:3]
    events = models.Event.objects.all().order_by("-date")[:3]
    if request.is_ajax():
        print("Request == Ajax")
        form = forms.InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponse(status=200)
        return http.HttpResponse(status=400)
    return render(
        request, "main/index.html", {"banner": banner, "news": news, "events": events}
    )


def news(request):
    banner = get_or_none(models.Banner, in_use=True)
    current_date = timezone.localtime().date()
    news = models.News.objects.filter(published__lte=current_date).order_by(
        "-published"
    )
    return render(request, "main/news.html", {"banner": banner, "news": news})


def news_article(request, slug):
    banner = get_or_none(models.Banner, in_use=True)
    article = models.News.objects.get(slug=slug)
    return render(
        request, "main/news-article.html", {"banner": banner, "article": article}
    )


def tour(request):
    banner = get_or_none(models.Banner, in_use=True)
    events = models.Event.objects.all().order_by("-date")
    return render(request, "main/tour.html", {"banner": banner, "events": events})


def music(request):
    banner = get_or_none(models.Banner, in_use=True)
    music = models.Music.objects.all()
    return render(request, "main/music.html", {"banner": banner, "music": music})


def media(request):
    banner = get_or_none(models.Banner, in_use=True)
    media = models.Media.objects.all()
    return render(request, "main/media.html", {"banner": banner, "media": media})


def about(request):
    banner = get_or_none(models.Banner, in_use=True)
    image = get_or_none(models.AboutImage, in_use=True)
    text = get_or_none(models.AboutText, in_use=True)
    video = get_or_none(models.AboutVideo, in_use=True)
    return render(
        request,
        "main/about.html",
        {"banner": banner, "image": image, "text": text, "video": video},
    )
