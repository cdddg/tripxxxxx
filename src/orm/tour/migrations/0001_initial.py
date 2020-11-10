# Generated by Django 3.1.3 on 2020-11-10 09:26

import core.constants
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourGroupBase',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('supplier_tour_code', models.CharField(max_length=256)),
                ('day_amount', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('is_recommend', models.IntegerField(verbose_name=core.constants.IsRecommendStatus['OFF'])),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplierbase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
