# Generated by Django 5.0.1 on 2024-07-04 16:46

import django.db.models.deletion
import wagtail_content_import.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0031_alter_articlepage_content_section_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DemoPage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Company name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Demo",
            },
            bases=("main.basepage", wagtail_content_import.models.ContentImportMixin),
        ),
    ]
