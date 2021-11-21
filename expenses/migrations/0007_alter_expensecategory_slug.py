# Generated by Django 3.2.9 on 2021-11-20 14:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_alter_expensecategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensecategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['created']),
        ),
    ]
