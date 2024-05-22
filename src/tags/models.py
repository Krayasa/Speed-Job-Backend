from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
