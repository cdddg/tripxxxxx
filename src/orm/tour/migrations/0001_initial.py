# Generated by Django 3.1.3 on 2020-11-14 09:47

import core.constants
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("supplier", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TourBase",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "tour_base",
            },
        ),
        migrations.CreateModel(
            name="TourGroupBase",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False
                    ),
                ),
                ("supplier_tour_code", models.CharField(max_length=256)),
                ("day_amount", models.IntegerField()),
                ("name", models.CharField(max_length=256)),
                ("is_recommend", models.IntegerField(verbose_name=core.constants.IsRecommendStatus["FALSE"])),
                ("score", models.FloatField()),
                ("currency", models.IntegerField()),
                ("default_price", models.FloatField()),
                (
                    "supplier",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="supplier.supplierbase"),
                ),
            ],
            options={
                "db_table": "tour_group_base",
            },
        ),
        migrations.CreateModel(
            name="TourGroupLocation",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.IntegerField()),
                ("option", models.IntegerField()),
                ("tour_group", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tour.tourgroupbase")),
            ],
            options={
                "db_table": "tour_group_location",
            },
        ),
        migrations.CreateModel(
            name="TourGroupTag",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("tag", models.CharField(max_length=128)),
                ("tour_group", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tour.tourgroupbase")),
            ],
            options={
                "db_table": "tour_group_tag",
                "unique_together": {("tour_group_id", "tag")},
            },
        ),
        migrations.CreateModel(
            name="TourGroupBucket",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False
                    ),
                ),
                ("date", models.DateField()),
                ("sku", models.IntegerField()),
                ("sell", models.IntegerField()),
                ("adult_price", models.FloatField()),
                ("child_price", models.FloatField()),
                ("baby_price", models.FloatField()),
                ("remark", models.CharField(max_length=1024)),
                ("transfer", models.IntegerField()),
                ("go_from", models.IntegerField()),
                ("back_from", models.IntegerField()),
                ("tour_group", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tour.tourgroupbase")),
            ],
            options={
                "db_table": "tour_group_bucket",
                "unique_together": {("tour_group_id", "date")},
            },
        ),
    ]
