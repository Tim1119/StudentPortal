# Generated by Django 3.2.9 on 2021-11-15 13:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='description', unique_with=['income_date', 'amount', 'source', 'created']),
        ),
    ]
