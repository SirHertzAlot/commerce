from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db import models

class User(AbstractUser):
    user_id = models.UUIDField(db_index=True,  primary_key=True, unique=True)
    user_first_name = models.CharField(name = 'First name', max_length = 60)
    user_street_address = models.CharField(name = 'Last name', max_length = 60)
    user_apartment_number = models.IntegerField(name='Apartment Number')
    user_city = models.CharField(name='City',max_length = 60)
    user_state = models.CharField(name='State',max_length = 60)

class Listing(models.Model):
    listing_id = models.UUIDField(db_index=True,  primary_key=True, unique=True)
    listing_name = models.CharField(name="Listing name", max_length=90)
    listing_category = models.CharField(name="Listing Category", max_length=90)
    listing_description = models.TextField(name="Listing Description")
    listing_start_time = models.DateTimeField(name="Time listing started",default=datetime.now())
    listing_duration = models.DurationField(name = 'Listing Time Remaining')
    listing_status = models.TextChoices("Active", "Expired")
    listing_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Bid(models.Model):
    bid_id = models.UUIDField(db_index=True, primary_key=True, unique=True)
    bid_amount = models.IntegerField(name='bid-amount')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comments(models.Model):
    comment_id = models.UUIDField(db_index=True, primary_key=True, unique=True)
    comment_data = models.TextField(name="Enter your comment")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)