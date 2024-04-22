# Generated by Django 4.2.9 on 2024-03-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discovery", "0009_remove_mediacredits_discovery_media_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="media",
            name="can_lend",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="media",
            name="progress",
            field=models.CharField(
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
        migrations.AddField(
            model_name="media",
            name="rating",
            field=models.CharField(
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
        migrations.AddField(
            model_name="media",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("i_own_a_physical_copy", "I own a physical copy"),
                    ("i_own_a_digital_copy", "I own a digital copy"),
                    ("i_borrowed_this_from_a_friend", "I borrowed this from a friend"),
                    (
                        "i_borrowed_this_from_the_local_library",
                        "I borrowed this from the local library",
                    ),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
