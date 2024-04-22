# Generated by Django 4.2.9 on 2024-04-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_initial"),
        (
            "discovery",
            "0040_remove_genres_source_type_remove_items_source_type_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activity",
            name="location",
        ),
        migrations.CreateModel(
            name="ActivityPlace",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="common.basemodel",
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="activity_places",
                        to="discovery.places",
                    ),
                ),
                (
                    "place_activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="activity_places",
                        to="discovery.activity",
                    ),
                ),
            ],
            options={
                "verbose_name": "Activity Place",
                "verbose_name_plural": "Activity Places",
            },
            bases=("common.basemodel",),
        ),
    ]
