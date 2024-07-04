# Generated by Django 5.0.1 on 2024-07-02 10:04

import wagtailmarkdown.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0026_alter_articlepage_rich_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="rich_text",
            field=wagtailmarkdown.fields.MarkdownField(
                blank=True, null=True, verbose_name="Content"
            ),
        ),
    ]