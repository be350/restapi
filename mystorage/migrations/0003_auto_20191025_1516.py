# Generated by Django 2.2.6 on 2019-10-25 06:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mystorage', '0002_album_fiels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fiels',
            new_name='Files',
        ),
    ]
