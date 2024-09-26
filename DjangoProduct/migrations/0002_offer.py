# Generated by Django 5.1 on 2024-09-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DjangoProduct", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=100)),
                ("discount", models.FloatField()),
            ],
        ),
    ]
