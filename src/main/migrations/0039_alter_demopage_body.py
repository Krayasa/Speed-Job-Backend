# Generated by Django 5.0.1 on 2024-07-04 18:44

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0038_alter_demopage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demopage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("my_heading_block", wagtail.blocks.CharBlock()),
                    ("my_paragraph_block", wagtail.blocks.RichTextBlock()),
                    (
                        "my_image_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "show_full_image",
                                    wagtail.blocks.BooleanBlock(required=False),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Content Sections",
            ),
        ),
    ]
