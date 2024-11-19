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


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('listing_name','listing_category','listing_description','listing_end_time','listing_image')
        labels = {
            'listing_name': 'Listing Name',
            'listing_category': 'Listing Category',
            'listing_description':'Listing Description',
            'listing_end_time': 'Listing End Time',
            'listing_image': 'Listing Image'
        }
        widgets = {
            'listing_name': forms.TextInput(attrs={'placeholder':'Enter the products name.'}),
            'listing_category': forms.TextInput(attrs={'placeholder':'Enter the products description.'}),
            'listing_description': forms.TextInput(attrs={'placeholder':'Enter a description for your product.'}),
            'listing_end_time': forms.DateTimeInput(attrs={'placeholder':''}),
        }

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
