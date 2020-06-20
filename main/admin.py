from django.contrib import admin

from . import models


@admin.register(models.AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ("description", "in_use")


@admin.register(models.AboutText)
class AboutTextAdmin(admin.ModelAdmin):
    list_display = ("content_preview", "in_use")


@admin.register(models.AboutVideo)
class AboutVideoAdmin(admin.ModelAdmin):
    list_display = ("description", "in_use")


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("text", "link", "in_use")


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "venue",
        "date",
    )
    date_heirarchy = "date"


@admin.register(models.Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "message", "received", "seen", "responded_to")
    date_heirarchy = "received"


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = [
        "description",
    ]


@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published")
    date_heirarchy = "published"


@admin.register(models.Press)
class PressAdmin(admin.ModelAdmin):
    list_display = ("source", "link")


admin.site.site_header = "Welcome Back"
admin.site.site_title = "Sick Wish"
admin.site.index_title = "Admin"
