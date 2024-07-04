from rest_framework import serializers
from wagtail.rich_text import expand_db_html

from . import ArticlePage
from .base_serializer import BasePageSerializer


class ArticlePageSerializer(BasePageSerializer):
    rich_text_1 = serializers.SerializerMethodField()

    class Meta:
        model = ArticlePage
        fields = BasePageSerializer.Meta.fields + ["rich_text_1","content_section"]

    # def get_rich_text(self, page):
    #     return expand_db_html(page.rich_text)

    def get_rich_text_1(self, page):
        return expand_db_html(page.rich_text_1)