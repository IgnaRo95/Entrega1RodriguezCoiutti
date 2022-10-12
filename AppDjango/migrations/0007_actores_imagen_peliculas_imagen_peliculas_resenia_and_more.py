# Generated by Django 4.1 on 2022-10-11 21:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDjango', '0006_remove_peliculas_resenia_remove_series_resenia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actores',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='resenia',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='series',
            name='resenia',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]