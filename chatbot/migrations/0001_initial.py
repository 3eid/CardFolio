# Generated by Django 5.0.6 on 2024-07-05 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq', models.TextField(blank=True)),
                ('about_me', models.TextField(blank=True)),
                ('work_examples', models.TextField(blank=True)),
                ('schedule', models.TextField(blank=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
