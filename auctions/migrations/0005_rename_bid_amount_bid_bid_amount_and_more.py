# Generated by Django 5.0.6 on 2024-06-28 10:05

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_listing_listing_endtime_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bid",
            old_name="bid-amount",
            new_name="bid_amount",
        ),
        migrations.AlterField(
            model_name="listing",
            name="Listing_endTime",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 28, 6, 5, 44, 639470)
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="Listing_startTime",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 28, 6, 5, 44, 639470), editable=False
            ),
        ),
    ]