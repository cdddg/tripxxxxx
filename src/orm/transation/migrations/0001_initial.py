# Generated by Django 3.1.3 on 2020-11-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TransationTourGroupBase",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "transation_tour_group_base",
            },
        ),
        migrations.CreateModel(
            name="TransationTourGroupBaseLog",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "transation_tour_group_log",
            },
        ),
    ]
