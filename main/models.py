import html

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils import timezone
from django.utils.html import strip_tags

from . import choices


class AboutImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField()
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Page Images"

    def save(self, *args, **kwargs):
        if self.in_use:
            try:
                temp = AboutImage.objects.get(in_use=True)
                if self != temp:
                    temp.in_use = False
                    temp.save()
            except AboutImage.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class AboutText(models.Model):
    content = RichTextField()
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Page Text"

    def save(self, *args, **kwargs):
        if self.in_use:
            try:
                temp = AboutText.objects.get(in_use=True)
                if self != temp:
                    temp.in_use = False
                    temp.save()
            except AboutText.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    @property
    def content_preview(self):
        return f"{strip_tags(html.unescape(self.content[:150]))} . . ."


class AboutVideo(models.Model):
    description = models.CharField(max_length=255)
    embed_html = models.TextField()
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "About Page Videos"

    def save(self, *args, **kwargs):
        if self.in_use:
            try:
                temp = AboutVideo.objects.get(in_use=True)
                if self != temp:
                    temp.in_use = False
                    temp.save()
            except AboutVideo.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class Banner(models.Model):
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    in_use = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.in_use:
            try:
                temp = Banner.objects.get(in_use=True)
                if self != temp:
                    temp.in_use = False
                    temp.save()
            except Banner.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=choices.STATES, default="ID")
    cover = models.PositiveIntegerField(null=True, blank=True)
    age_restrictions = models.CharField(
        max_length=2, choices=choices.RESTRICTIONS, default="AA"
    )

    @property
    def location(self):
        return f"{self.city}, {self.state}"


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
    image = models.ImageField()
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    published = models.DateField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "News Posts"

    @property
    def preview(self):
        return truncatewords(strip_tags(html.unescape(self.content)), 50)[:-1]


class Press(models.Model):
    source = models.CharField(max_length=255)
    image = models.ImageField()
    content = models.TextField()
    link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Press"
