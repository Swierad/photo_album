# Generated by Django 3.0.7 on 2020-09-26 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_album', '0003_remove_photo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='creation_date',
        ),
    ]
