from django import http
from django.shortcuts import render
from django.utils import timezone

from . import models


def index(request):
    current_date = timezone.localtime().date()
    news = models.News.objects.filter(published__lte=current_date).order_by(
        "-published"
    )[:3]
    events = models.Event.objects.all().order_by("-date")
    if request.is_ajax():
        form = forms.LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponse(status=200)
        return http.HttpResponse(status=400)
    return render(request, "main/index.html", {"news": news, "events": events})
