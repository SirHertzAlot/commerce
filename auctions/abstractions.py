from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.forms import BidForm


def returnGetListing(request, valuesDict, is_owner):
    """
    Return a listing using the listing's ID to retrieve it's value. 
    This function expects a dictionary of values (Which is the default return value from SQL for retrieving a single listing.), and a boolean value for is_owner.
    :model:`auctions.models.Listing`.
    """
    return render(request, "auctions/getListing.html", {
                "Listing_name": valuesDict["Listing_name"],
                "Listing_description": valuesDict["Listing_description"],
                "Listing_category": valuesDict["Listing_category"],
                "Listing_startTime": valuesDict["Listing_startTime"],
                "Listing_duration": valuesDict["Listing_duration"],
                "BidForm": BidForm(),
                "is_owner": is_owner
            })

def postForm(request, formString:str):
    """
    The logic that takes a form's data, validates it, and also saves the cleaned data to it's appropriate SQLite table.
    If successful, you will be redirected.
    :model:`auctions.models`,
    """
    if request.method == "POST":
        form = f"{formString}Form"(request.POST)
        if form.is_valid():
                #Save valid listing request
            f"{formString}".save(form.cleaned_data)

                # Redirect user to list of entries
            return HttpResponseRedirect(reverse("index")) 