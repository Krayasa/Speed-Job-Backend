from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail_content_import.models import ContentImportMixin
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail_content_import.mappers.converters import ImageConverter, RichTextConverter, TableConverter, TextConverter
from wagtail_content_import.mappers.streamfield import StreamFieldMapper

from wagtail.models import PageManager
from wagtail.fields import RichTextField,StreamField

from .base import BasePage
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.contrib.table_block.blocks import TableBlock



class MyMapper(StreamFieldMapper):
    image = ImageConverter('my_image_block')
    heading = TextConverter('my_heading_block')
    html = RichTextConverter('my_paragraph_block')
    # table = TableConverter('my_table_block')


section_blocks = [("my_heading_block",CharBlock()),
     ("my_paragraph_block" ,RichTextBlock()),
    ( "my_image_block", ImageChooserBlock()),]


        
class DemoPage(HeadlessPreviewMixin, BasePage, ContentImportMixin):
    rich_text_1 = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    # rich_text = MarkdownField(verbose_name=_("Content"), blank=True, null=True)
    body = StreamField(
        # [("my_heading_block", CharBlock()),
        #  ("my_paragraph_block", RichTextBlock()),
        #  ("my_image_block", ImageChooserBlock()),
        #  ("my_table_block", TableBlock()),
        # ],
        section_blocks,use_json_field=True, blank=True, null=True, verbose_name=_("Content Sections"))


    content_panels = BasePage.content_panels + [FieldPanel("rich_text_1"),FieldPanel("body", classname="full")]

    extra_panels = BasePage.extra_panels
    mapper_class = MyMapper
    # serializer_class = "main.pages.ArticlePageSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("Demo")

        
