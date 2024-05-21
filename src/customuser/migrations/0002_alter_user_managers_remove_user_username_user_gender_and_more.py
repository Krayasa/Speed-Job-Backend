# Generated by Django 5.0.1 on 2024-05-21 13:02

import customuser.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customuser", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", customuser.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(blank=True, default="", max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                default="employer",
                error_messages={"required": "Role must be provided"},
                max_length=12,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "A user with that email already exists."},
                max_length=254,
                unique=True,
            ),
        ),
    ]