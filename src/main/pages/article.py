from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField,StreamField
from main.blocks.blocks import APIImageChooserBlock
from wagtail.blocks import RichTextBlock
from wagtail.models import PageManager
from django.db import models
from customimage.models import CustomImage
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail_content_import.models import ContentImportMixin
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail_content_import.mappers.converters import RichTextConverter
from wagtail_content_import.mappers.streamfield import StreamFieldMapper

from .base import BasePage
from main.blocks import section_blocks
# from wagtailmarkdown.fields import MarkdownField

class MyMapper(StreamFieldMapper):
    html = RichTextConverter('my_paragraph_block')


class ArticlePage(HeadlessPreviewMixin, BasePage, ContentImportMixin):
    rich_text_1 = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    cover_image = models.ForeignKey(CustomImage, null=True, blank=True, on_delete=models.SET_NULL, related_name="+", verbose_name=_("Cover Image"))
    content_section = StreamField(section_blocks,use_json_field=True, blank=True, null=True, verbose_name=_("Content Sections"))
    body = StreamField([
        ("cover_image", APIImageChooserBlock(required=False,
            label="Image",
            help_text="Pick a cover image for blog",
        )),
        ("my_paragraph_block", RichTextBlock(
            required=False,
            label="Content",
            help_text="Write content for the article",
        )),
    ],use_json_field=True, blank=True, null=True, verbose_name=_("Article Sections"))


    content_panels = BasePage.content_panels + [FieldPanel("rich_text_1"),FieldPanel("content_section", classname="full"),FieldPanel("body", classname="full"),FieldPanel("cover_image")]

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.ArticlePageSerializer"
    mapper_class = MyMapper

    objects: PageManager

    class Meta:
        verbose_name = _("Article")
