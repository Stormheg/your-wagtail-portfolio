# Generated by Django 4.2.3 on 2023-07-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_blogpostpage_body_blogpostpage_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="your_name",
            field=models.CharField(
                default="Jane Appleseed", max_length=32, verbose_name="your name"
            ),
            preserve_default=False,
        ),
    ]