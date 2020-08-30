from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, reverse
from django.utils import timezone
from main import views, models

from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "articles": GenericSitemap(
        {
            "queryset": models.News.objects.filter(
                published__lte=timezone.now().date()
            ),
            "date_field": "published",
        },
        priority=0.9,
        protocol="https",
    ),
}


urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
