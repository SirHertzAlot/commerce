# Generated by Django 5.0.6 on 2024-06-28 06:06

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_alter_listing_listing_starttime_watchlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="Listing_endTime",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 28, 2, 6, 40, 810418)
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="Listing_startTime",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 28, 2, 6, 40, 810418), editable=False
            ),
        ),
        migrations.AlterField(
            model_name="watchlist",
            name="add_to_list",
            field=models.BooleanField(default=False),
        ),
    ]
