# Generated by Django 4.1 on 2022-10-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDjango', '0004_alter_peliculas_resenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='resenia',
            field=models.TextField(blank=True, null=True),
        ),
    ]