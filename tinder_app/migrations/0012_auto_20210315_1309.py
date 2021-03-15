# Generated by Django 3.1.7 on 2021-03-15 12:09

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('tinder_app', '0011_dog_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dogbreed',
            options={'ordering': ['breed']},
        ),
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[320, 240], upload_to='pictures'),
        ),
    ]
