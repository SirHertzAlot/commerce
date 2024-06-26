# Generated by Django 5.0.6 on 2024-06-26 07:20

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Expired', 'Expired')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Listing_startTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 3, 20, 21, 645832)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
