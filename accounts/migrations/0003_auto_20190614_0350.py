# Generated by Django 2.2.1 on 2019-06-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_testimonial_client_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='client_image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]