# Generated by Django 4.1.4 on 2022-12-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("FullName", models.CharField(max_length=25)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Technology", models.CharField(max_length=30)),
            ],
            options={"db_table": "user",},
        ),
    ]
