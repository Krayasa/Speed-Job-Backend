import typing

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path, re_path
from django.views import defaults as default_views
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from main.views.error_500 import error_500_view
from main.views.page_not_found import PageNotFoundView
from nextjs.api import api_router
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


handler404 = PageNotFoundView.as_view()
handler500 = error_500_view

URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]

schema_view = get_schema_view(
    openapi.Info(
        title="Jobs Portal API",
        default_version="v1",
        description="Jobs Portal Api Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns: URLList = []

if settings.DEBUG:
    urlpatterns += [
        path(
            "wt/400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),  # NOQA
        path(
            "wt/403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),  # NOQA
        path(
            "wt/404/", handler404, kwargs={"exception": Exception("Page not Found")}
        ),  # NOQA
        path(
            "wt/500/", handler500, kwargs={"exception": Exception("Internal error")}
        ),  # NOQA
    ]

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path("wt/__debug__/", include(debug_toolbar.urls))]


def trigger_error(request):
    division_by_zero = 1 / 0  # NOQA: F841


def health_check(request):
    from django.http import HttpResponse
    return HttpResponse("Its alive")


urlpatterns += [
    path("wt/sentry-debug/", trigger_error),
    path(settings.ADMIN_URL, admin.site.urls),
    path("wt/api/nextjs/v1/", api_router.urls),
    path("wt/cms/", include(wagtailadmin_urls)),
    path("wt/documents/", include(wagtaildocs_urls)),
    path("wt/sitemap.xml", sitemap, name="sitemap"),
    path("wt/health-check/", health_check, name="health_check"),
     path(
        "wt/api/",
        include(
            [
                path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
                path("", include("customuser.api.urls")),
                path("", include("jobs.api.urls")),
                path("", include("tags.api.urls")),
                # path('auth/oauth/', include('rest_framework_social_oauth2.urls'))
            ]
        ),
    ),
]

urlpatterns += [re_path(r"", include(wagtail_urls))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
