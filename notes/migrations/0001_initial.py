# Generated by Django 3.2.9 on 2021-11-21 10:02

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['created'])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('note_order', models.IntegerField(blank=True, help_text='leave blank if it has no order', null=True)),
                ('content', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=['created', 'profile', 'course'])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, help_text='leave blank if it is a stand alone note', null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.course')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
