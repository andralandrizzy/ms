# Generated by Django 2.2.1 on 2019-06-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]