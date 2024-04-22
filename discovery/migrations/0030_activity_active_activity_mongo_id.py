# Generated by Django 4.2.9 on 2024-04-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discovery", "0029_careerinterests_active_careerinterests_mongo_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="activity",
            name="mongo_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
