# Generated by Django 5.0.1 on 2024-07-04 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0028_articlepage_rich_text_1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="articlepage",
            name="rich_text",
        ),
    ]
