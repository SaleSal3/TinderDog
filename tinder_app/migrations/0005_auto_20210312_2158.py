# Generated by Django 3.1.7 on 2021-03-12 20:58

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('tinder_app', '0004_auto_20210311_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[320, 240], upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='dog',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[320, 240], upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='dog',
            name='image4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[320, 240], upload_to='pictures'),
        ),
    ]
