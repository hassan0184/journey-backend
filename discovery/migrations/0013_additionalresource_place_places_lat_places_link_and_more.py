# Generated by Django 4.2.9 on 2024-03-17 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("discovery", "0012_additionalresource_character_characters_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="additionalresource",
            name="place",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="additional_resources",
                to="discovery.places",
            ),
        ),
        migrations.AddField(
            model_name="places",
            name="lat",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="places",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="places",
            name="lon",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="characters",
            name="source_type",
            field=models.CharField(
                blank=True,
                choices=[("native", "Native"), ("mentioned", "Mentioned")],
                max_length=50,
                null=True,
                verbose_name="Is this character mentioned in this media or native to this media?",
            ),
        ),
    ]
