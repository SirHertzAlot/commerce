from datetime import datetime

from django import forms

from auctions.models import Bid, Comments, Listing, Watchlist


class StatusForm(forms.ModelForm):
    """
    :description:`The form used to change the status of a listing from active to exposed. :model:`StatusForm.forms.ModelForm`.`
    :type:`Boolean`
    """

    class Meta:
        model = Listing
        fields = ["listing_status"]


class CreateListingForm(forms.Form):
    listing_name = forms.CharField(label="Listing_name", max_length=90, required=True)
    listing_description = forms.Textarea()
    listing_category = forms.CharField(
        label="Listing_category", max_length=90, required=True
    )
    listing_status = forms.CharField(initial="Active")
    listing_start_time = forms.DateTimeField(initial=datetime.now())
    listing_duration = forms.TimeField(label="Listing_duration", required=True)


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["bid_amount"]


class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ["add_to_list"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["Comment"]
