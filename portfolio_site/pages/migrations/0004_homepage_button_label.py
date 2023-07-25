# Generated by Django 4.2.3 on 2023-07-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_homepage_button_page"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="button_label",
            field=models.CharField(
                default="", max_length=32, verbose_name="button label"
            ),
            preserve_default=False,
        ),
    ]