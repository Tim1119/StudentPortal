# Generated by Django 3.2.9 on 2021-11-13 21:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preference',
            new_name='UserPreferences',
        ),
    ]
