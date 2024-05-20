from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField,StreamField
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin

from .base import BasePage
from main.blocks import section_blocks


class ArticlePage(HeadlessPreviewMixin, BasePage):
    rich_text = RichTextField(blank=True, null=True, verbose_name=_("Rich text"))
    content_section = StreamField(section_blocks,use_json_field=True,)

    content_panels = BasePage.content_panels + [FieldPanel("rich_text"),FieldPanel("content_section", classname="full"),]

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.ArticlePageSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("Article")
