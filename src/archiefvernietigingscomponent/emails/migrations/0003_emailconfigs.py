# Generated by Django 2.2.12 on 2021-03-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0002_emailpreference"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailConfigs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "municipality",
                    models.CharField(
                        help_text="The municipality on behalf of which the emails are sent.",
                        max_length=200,
                        verbose_name="municipality",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
