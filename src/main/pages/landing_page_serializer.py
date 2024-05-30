from rest_framework import serializers
from wagtail.rich_text import expand_db_html


from . import LandingPage
from .base_serializer import BasePageSerializer


class LandingPageSerializer(BasePageSerializer):
    # body = serializers.SerializerMethodField()
    # hero_section = HeroSectionSerializer()


    class Meta:
        model = LandingPage
        fields = BasePageSerializer.Meta.fields + ["body", "feed_image"]

    def get_rich_text(self, page):
        return expand_db_html(page.rich_text)
