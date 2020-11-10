# Generated by Django 3.1.3 on 2020-11-10 09:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberFavorite',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.memberbase')),
                ('tour_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourgroupbase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]