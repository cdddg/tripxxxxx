# Generated by Django 3.1.3 on 2020-11-10 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierBase',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('score_amount', models.IntegerField()),
                ('food_score', models.CharField(max_length=256)),
                ('traffic_score', models.CharField(max_length=256)),
                ('scheduler_score', models.CharField(max_length=256)),
                ('tour_guide_score', models.CharField(max_length=256)),
                ('stay_score', models.CharField(max_length=256)),
                ('logo_url', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]