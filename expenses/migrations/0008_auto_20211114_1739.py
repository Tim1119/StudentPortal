# Generated by Django 3.2.9 on 2021-11-14 16:39

import autoslug.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_alter_expense_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='description', unique_with=['expense_date', 'amount', 'category', 'created']),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(default=datetime.datetime(2021, 11, 14, 16, 39, 1, 560727, tzinfo=utc), max_length=800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(help_text='yyyy-mm-dd'),
        ),
    ]
