# Generated by Django 5.1.5 on 2025-02-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorial", "0002_alter_coursetype_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursetype",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
