# Generated by Django 5.0.3 on 2024-03-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmez', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='runtime',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='year',
            field=models.CharField(max_length=255),
        ),
    ]
