# Generated by Django 4.2.9 on 2024-02-19 11:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseModel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="AgeGroup",
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
                ("label", models.CharField(max_length=50, unique=True)),
                ("min_age", models.IntegerField()),
                ("max_age", models.IntegerField()),
            ],
            options={
                "verbose_name": "Age Group",
                "verbose_name_plural": "Age Group",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="Ethnicity",
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
                ("label", models.CharField(max_length=50, unique=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Ethnicity",
                "verbose_name_plural": "Ethnicity",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="Gender",
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
                ("label", models.CharField(max_length=50, unique=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Gender",
                "verbose_name_plural": "Gender",
            },
            bases=("common.basemodel",),
        ),
    ]
