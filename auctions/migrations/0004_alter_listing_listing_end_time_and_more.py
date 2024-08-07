# Generated by Django 5.0.6 on 2024-07-19 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_listing_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 19, 25, 11, 943911, tzinfo=datetime.timezone.utc), verbose_name='Listing_endTime'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Listing_image'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 19, 25, 11, 943911, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Listing_startTime'),
        ),
    ]
