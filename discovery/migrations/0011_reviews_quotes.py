# Generated by Django 4.2.9 on 2024-03-17 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_initial"),
        ("discovery", "0010_media_can_lend_media_progress_media_rating_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                ("review", models.TextField(blank=True, null=True)),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_reviews",
                        to="discovery.media",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="Quotes",
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
                ("quote", models.TextField(blank=True, null=True)),
                ("said_by", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_quotes",
                        to="discovery.media",
                    ),
                ),
            ],
            options={
                "verbose_name": "Quote",
                "verbose_name_plural": "Quotes",
            },
            bases=("common.basemodel",),
        ),
    ]
