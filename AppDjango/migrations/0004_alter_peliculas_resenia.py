# Generated by Django 4.1 on 2022-10-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDjango', '0003_peliculas_resenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='resenia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
