# Generated by Django 3.0.7 on 2020-09-26 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_album', '0002_auto_20200926_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]
