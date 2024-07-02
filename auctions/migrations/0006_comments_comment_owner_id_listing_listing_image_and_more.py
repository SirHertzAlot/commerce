# Generated by Django 5.0.6 on 2024-07-02 04:39

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_rename_bid_amount_bid_bid_amount_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="comment_owner_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="Listing_image",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="listing",
            name="Listing_endTime",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 7, 2, 0, 39, 12, 747147)
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="Listing_startTime",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 7, 2, 0, 39, 12, 747147), editable=False
            ),
        ),
    ]
