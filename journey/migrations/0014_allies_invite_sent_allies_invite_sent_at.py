# Generated by Django 4.2.9 on 2024-03-21 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0013_alter_allies_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='allies',
            name='invite_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='allies',
            name='invite_sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
