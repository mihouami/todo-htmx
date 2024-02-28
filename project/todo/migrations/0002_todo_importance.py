# Generated by Django 5.0.1 on 2024-02-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="importance",
            field=models.CharField(
                choices=[
                    ("V", "Very Important"),
                    ("I", "Important"),
                    ("N", "Not Important"),
                ],
                max_length=1,
                null=True,
            ),
        ),
    ]