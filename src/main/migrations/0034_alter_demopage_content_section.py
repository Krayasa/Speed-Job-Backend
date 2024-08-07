# Generated by Django 5.0.1 on 2024-07-04 16:52

import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0033_remove_demopage_company_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demopage",
            name="content_section",
            field=wagtail.fields.StreamField(
                [
                    ("my_heading_block", wagtail.blocks.CharBlock()),
                    ("my_paragraph_block", wagtail.blocks.RichTextBlock()),
                    ("my_image_block", wagtail.images.blocks.ImageChooserBlock()),
                    ("my_table_block", wagtail.contrib.table_block.blocks.TableBlock()),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Content Sections",
            ),
        ),
    ]
