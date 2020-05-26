from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils import timezone

from . import choices


class AboutImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField()
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Page Images"


class AboutText(models.Model):
    content = models.TextField()
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Page Text"


class AboutVideo(models.Model):
    description = models.CharField(max_length=255)
    embed_html = models.TextField()
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Page Videos"


class Banner(models.Model):
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    in_use = models.BooleanField(default=False)


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=choices.STATES, default="ID")
    cover = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    age_restrictions = models.CharField(
        max_length=2, choices=choices.RESTRICTIONS, default="AA"
    )


class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    received = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    responded_to = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Inquiries"


class Media(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField()

    class Meta:
        verbose_name_plural = "Media Page Images"


class Music(models.Model):
    title = models.CharField(max_length=255)
    embed_html = models.TextField()

    class Meta:
        verbose_name_plural = "Embedded Albums"


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "News Posts"

    @property
    def preview(self):
        return truncatewords(self.content, 50)[:-1]


class Press(models.Model):
    source = models.CharField(max_length=255)
    image = models.ImageField()
    content = models.TextField()
    link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Press"
