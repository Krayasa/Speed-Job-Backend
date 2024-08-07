# Generated by Django 5.0.1 on 2024-07-08 08:46

import main.blocks.blocks
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0043_articlepage_body_alter_articlepage_content_section_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("my_image_block", main.blocks.blocks.APIImageChooserBlock()),
                    ("my_paragraph_block", wagtail.blocks.RichTextBlock()),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Article Sections",
            ),
        ),
    ]
