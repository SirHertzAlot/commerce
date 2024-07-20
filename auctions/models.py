import uuid
import datetime

from django.utils import timezone
from django.utils.timezone import make_aware
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Stores a single user object. :model:`auth.User`.
    """

    user_id = models.UUIDField(
        default=uuid.uuid4, db_index=True, editable=False, primary_key=True, unique=True
    )
    user_street_address = models.CharField(name="street_address", max_length=60)
    user_city = models.CharField(name="city", max_length=60)
    user_state = models.CharField(name="state", max_length=60)


class Listing(models.Model):
    """
    Stores a single listing object. :model:`listing.Listing`.
    """
    now = make_aware(datetime.datetime.now())
    class Status(models.TextChoices):
        ACTIVE = "Active"
        EXPIRED = "Expired"

    listing_id = models.UUIDField(
        default=uuid.uuid4, db_index=True, editable=False, primary_key=True, unique=True
    )
    listing_name = models.CharField("Listing_name", max_length=90, blank=True)
    listing_category = models.CharField("Listing_category", max_length=90, blank=True)
    listing_description = models.TextField("Listing_description", blank=True)
    listing_image = models.ImageField("Listing_image", upload_to="images", null=True, blank=True)
    listing_start_time = models.DateTimeField(
    "Listing_startTime", default=now, editable=False
    )
    listing_end_time = models.DateTimeField(
    "Listing_endTime", default=now
    )
    listing_duration = models.DurationField("Listing_duration", default=60000)
    listing_status = models.CharField(
        choices=Status, default=Status.ACTIVE, max_length=10
    )
    listing_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Bid(models.Model):
    """
    Stores a single bid object. :model:`bid.Bid`.
    """

    bid_id = models.UUIDField(
        default=uuid.uuid4, db_index=True, primary_key=True, unique=True
    )
    bid_amount = models.IntegerField(name="bid_amount")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Watchlist(models.Model):
    """
    Stores a single bid object. :model:`bid.Bid`.
    """

    class Add(models.TextChoices):
        ADD = "Add"

    list_item_id = models.UUIDField(
        default=uuid.uuid4, db_index=True, primary_key=True, unique=True
    )
    add_to_list = models.BooleanField(name="add_to_list", default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Comments(models.Model):
    """
    Stores a single comment object. :model:`comment.Comment`.
    """

    comment_id = models.UUIDField(
        default=uuid.uuid4, db_index=True, primary_key=True, unique=True
    )
    comment_data = models.TextField(name="Comment")
    comment_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
