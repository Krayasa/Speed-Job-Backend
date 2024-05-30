from main.blocks import section_blocks
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField
from wagtail.models import PageManager
from django.db import models
from customimage.models import CustomImage

from wagtail_headless_preview.models import HeadlessPreviewMixin
from django.utils.translation import gettext_lazy as _
from .base import BasePage

class LandingPage(HeadlessPreviewMixin, BasePage):
    body = StreamField(section_blocks,use_json_field=True,)
    feed_image = models.ForeignKey(CustomImage, on_delete=models.SET_NULL, null=True)


    api_fields = [
        APIField("body"),
        APIField("feed_image"),
    ]

    search_fields = Page.search_fields + [

        index.SearchField("body"),
    ]

    extra_panels = BasePage.extra_panels

    content_panels = Page.content_panels + [
        # FieldPanel("intro"),
        FieldPanel("body", classname="full"),
        FieldPanel("feed_image"),
    ]
    serializer_class = "main.pages.landing_page_serializer.LandingPageSerializer"
    objects: PageManager
    class Meta:
        verbose_name = _("Business Landing Page")
