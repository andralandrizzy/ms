# Generated by Django 2.2.1 on 2019-06-13 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('date_create', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]