# Generated by Django 4.2.3 on 2023-07-21 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        ("pages", "0002_homepageskillplacement"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="button_page",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="button page",
            ),
        ),
    ]
