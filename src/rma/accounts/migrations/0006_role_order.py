# Generated by Django 2.2.12 on 2020-07-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_auto_20200713_1550"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=1, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
    ]