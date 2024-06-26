# Generated by Django 4.2.9 on 2024-03-17 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("discovery", "0014_rename_place_type_places_o_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="additionalresource",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="additional_resources",
                to="discovery.items",
            ),
        ),
    ]
