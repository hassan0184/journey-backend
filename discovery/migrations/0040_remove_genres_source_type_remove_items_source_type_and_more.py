# Generated by Django 4.2.9 on 2024-04-09 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_initial"),
        (
            "discovery",
            "0039_remove_media_places_alter_mediaplace_discovery_media_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genres",
            name="source_type",
        ),
        migrations.RemoveField(
            model_name="items",
            name="source_type",
        ),
        migrations.RemoveField(
            model_name="media",
            name="activities",
        ),
        migrations.RemoveField(
            model_name="media",
            name="career_interests",
        ),
        migrations.RemoveField(
            model_name="media",
            name="genres",
        ),
        migrations.RemoveField(
            model_name="media",
            name="items",
        ),
        migrations.RemoveField(
            model_name="media",
            name="purchase_oppurtunities",
        ),
        migrations.RemoveField(
            model_name="media",
            name="related_media",
        ),
        migrations.RemoveField(
            model_name="media",
            name="themes",
        ),
        migrations.RemoveField(
            model_name="media",
            name="time_periods",
        ),
        migrations.RemoveField(
            model_name="media",
            name="topics",
        ),
        migrations.RemoveField(
            model_name="timeperiods",
            name="source_type",
        ),
        migrations.RemoveField(
            model_name="topics",
            name="source_type",
        ),
        migrations.CreateModel(
            name="RelatedMedia",
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
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="discovery_related_media",
                        to="discovery.media",
                    ),
                ),
                (
                    "related_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_media",
                        to="discovery.media",
                    ),
                ),
            ],
            options={
                "verbose_name": "Related Media",
                "verbose_name_plural": "Related Media",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaTopic",
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
                    "source_type",
                    models.CharField(
                        blank=True,
                        choices=[("native", "Native"), ("mentioned", "Mentioned")],
                        max_length=50,
                        null=True,
                        verbose_name="Is this topic mentioned in this media or native to this media?",
                    ),
                ),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_topics",
                        to="discovery.media",
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_topics",
                        to="discovery.topics",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Topic",
                "verbose_name_plural": "Media Topics",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaTimePeriod",
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
                    "source_type",
                    models.CharField(
                        blank=True,
                        choices=[("native", "Native"), ("mentioned", "Mentioned")],
                        max_length=50,
                        null=True,
                        verbose_name="Is this time period mentioned in this media or native to this media?",
                    ),
                ),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_time_periods",
                        to="discovery.media",
                    ),
                ),
                (
                    "time_period",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_time_periods",
                        to="discovery.timeperiods",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Time Period",
                "verbose_name_plural": "Media Time Periods",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaTheme",
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
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_themes",
                        to="discovery.media",
                    ),
                ),
                (
                    "theme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_themes",
                        to="discovery.themes",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Theme",
                "verbose_name_plural": "Media Themes",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaPurchaseOppurtunity",
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
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_purchase_oppurtunities",
                        to="discovery.media",
                    ),
                ),
                (
                    "purchase_oppurtunity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_purchase_oppurtunities",
                        to="discovery.purchaseoppurtunities",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Purchase Oppurtunity",
                "verbose_name_plural": "Media Purchase Oppurtunities",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaItem",
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
                    "source_type",
                    models.CharField(
                        blank=True,
                        choices=[("native", "Native"), ("mentioned", "Mentioned")],
                        max_length=50,
                        null=True,
                        verbose_name="Is this item mentioned in this media or native to this media?",
                    ),
                ),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_items",
                        to="discovery.media",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_items",
                        to="discovery.items",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Item",
                "verbose_name_plural": "Media Items",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaGenre",
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
                    "source_type",
                    models.CharField(
                        blank=True,
                        choices=[("native", "Native"), ("mentioned", "Mentioned")],
                        max_length=50,
                        null=True,
                        verbose_name="Is this genre mentioned in this media or native to this media?",
                    ),
                ),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_genres",
                        to="discovery.media",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_genres",
                        to="discovery.genres",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Genre",
                "verbose_name_plural": "Media Genres",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaCareerInterest",
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
                    "career_interest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_career_interests",
                        to="discovery.careerinterests",
                    ),
                ),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_career_interests",
                        to="discovery.media",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Career Interest",
                "verbose_name_plural": "Media Career Interests",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="MediaActivity",
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
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_activities",
                        to="discovery.media",
                    ),
                ),
                (
                    "media_activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_activities",
                        to="discovery.activity",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media Activity",
                "verbose_name_plural": "Media Activities",
            },
            bases=("common.basemodel",),
        ),
    ]
