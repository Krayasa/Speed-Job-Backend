# Generated by Django 5.0.1 on 2024-05-31 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customdocument", "0002_initial"),
        ("customuser", "0005_remove_user_gender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="cv",
        ),
        migrations.RemoveField(
            model_name="user",
            name="passport",
        ),
        migrations.AddField(
            model_name="user",
            name="document1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document1",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document10",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document10",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document2",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document3",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document4",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document5",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document6",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document6",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document7",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document7",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document8",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document8",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="document9",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document9",
                to="customdocument.customdocument",
            ),
        ),
    ]
