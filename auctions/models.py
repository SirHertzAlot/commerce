from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db import models
import uuid

class User(AbstractUser):
    """
        Stores a single user object. :model:`auth.User`.
    """
    user_id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False,  primary_key=True, unique=True)
    user_street_address = models.CharField(name = 'street_address', max_length = 60)
    user_city = models.CharField(name='city',max_length = 60)
    user_state = models.CharField(name='state',max_length = 60)

class Listing(models.Model):
    """
        Stores a single listing object. :model:`listing.Listing`.
    """
    class Status(models.TextChoices):
        ACTIVE = "Active"
        EXPIRED = "Expired"
    listing_id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False,  primary_key=True, unique=True)
    listing_name = models.CharField(name="Listing_name", max_length=90)
    listing_category = models.CharField(name="Listing_category", max_length=90)
    listing_description = models.TextField(name="Listing_description")
    listing_start_time = models.DateTimeField(name="Listing_startTime",default=datetime.now())
    listing_duration = models.DurationField(name = 'Listing_duration')
    listing_status = models.CharField(choices=Status, default=Status.ACTIVE, max_length=10)
    listing_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Bid(models.Model):
    """
        Stores a single bid object. :model:`bid.Bid`.
    """
    bid_id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True, unique=True)
    bid_amount = models.IntegerField(name="bid-amount")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Watchlist(models.Model):
    """
        Stores a single bid object. :model:`bid.Bid`.
    """
    class Add(models.TextChoices):
        ADD = "Add"
    list_item_id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True, unique=True)
    add_to_list = models.CharField(choices=Add, max_length=3)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Comments(models.Model):
    """
        Stores a single comment object. :model:`comment.Comment`.
    """
    comment_id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True, unique=True)
    comment_data = models.TextField(name="Comment")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)