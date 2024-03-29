# Generated by Django 5.0.3 on 2024-03-09 19:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id_filmes', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
            ],
        ),
    ]
