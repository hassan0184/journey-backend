# Generated by Django 4.2.9 on 2024-04-12 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_initial"),
        ("discovery", "0041_remove_activity_location_activityplace"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="media",
            name="can_lend",
        ),
        migrations.RemoveField(
            model_name="media",
            name="progress",
        ),
        migrations.RemoveField(
            model_name="media",
            name="rating",
        ),
        migrations.RemoveField(
            model_name="media",
            name="status",
        ),
        migrations.CreateModel(
            name="UserExperience",
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
                    "progress",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("not_started", "Not Started"),
                            ("in_progress", "In Progress"),
                            ("completed", "Completed"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("i_own_a_physical_copy", "I own a physical copy"),
                            ("i_own_a_digital_copy", "I own a digital copy"),
                            (
                                "i_borrowed_this_from_a_friend",
                                "I borrowed this from a friend",
                            ),
                            (
                                "i_borrowed_this_from_the_local_library",
                                "I borrowed this from the local library",
                            ),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "rating",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1", "Okay"),
                            ("2", "Good"),
                            ("4", "Great"),
                            ("5", "Excellent"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("can_lend", models.BooleanField(default=False)),
                (
                    "discovery_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_experiences",
                        to="discovery.media",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Experience",
                "verbose_name_plural": "User Experiences",
            },
            bases=("common.basemodel",),
        ),
    ]
