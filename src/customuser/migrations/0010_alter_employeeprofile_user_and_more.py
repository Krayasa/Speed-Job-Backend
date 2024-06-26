# Generated by Django 5.0.1 on 2024-06-10 07:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customuser", "0009_remove_employeeprofile_website_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="employerprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employer_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
