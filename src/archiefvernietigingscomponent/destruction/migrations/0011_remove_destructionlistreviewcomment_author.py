# Generated by Django 2.2.12 on 2021-03-02 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("destruction", "0010_auto_20210225_1711"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="destructionlistreviewcomment", name="author",
        ),
    ]
