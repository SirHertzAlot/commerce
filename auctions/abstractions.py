from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.forms import BidForm, CommentForm, WatchlistForm


def returnBidResponse(request, valuesDict, is_owner, commentsDict, bidsDict, error):
    """
    Return a listing using the listing's ID to retrieve it's value.
    This function expects a dictionary of values (Which is the default return value from SQL for retrieving a single listing.), and a boolean value for is_owner.
    :model:`auctions.models.Listing`.
    """
    if error:
        return render(
            request,
            "auctions/getListing.html",
            {
                "Listing_id": valuesDict.listing_id,
                "Listing_name": valuesDict.Listing_name,
                "Listing_description": valuesDict.Listing_description,
                "Listing_category": valuesDict.Listing_category,
                "Listing_status": valuesDict.listing_status,
                "Listing_startTime": valuesDict.Listing_startTime,
                "Listing_endTime": valuesDict.Listing_endTime,
                "Listing_duration": valuesDict.Listing_duration,
                "Listing_image": valuesDict.Listing_image,
                "bids": bidsDict,
                "comments": commentsDict,
                "WatchlistForm": WatchlistForm(),
                "CommentForm": CommentForm(),
                "BidForm": BidForm(),
                "is_owner": is_owner,
                "error": error,
            },
        )
    return render(
        request,
        "auctions/getListing.html",
        {
            "Listing_id": valuesDict.listing_id,
            "Listing_name": valuesDict.Listing_name,
            "Listing_description": valuesDict.Listing_description,
            "Listing_category": valuesDict.Listing_category,
            "Listing_status": valuesDict.listing_status,
            "Listing_startTime": valuesDict.Listing_startTime,
            "Listing_endTime": valuesDict.Listing_endTime,
            "Listing_duration": valuesDict.Listing_duration,
            "bids": bidsDict,
            "comments": commentsDict,
            "WatchlistForm": WatchlistForm(),
            "CommentForm": CommentForm(),
            "BidForm": BidForm(),
            "is_owner": is_owner,
        },
    )


def returnGetListing(request, valuesDict, is_owner, commentsDict, bidsDict, error):
    """
    Return a listing using the listing's ID to retrieve it's value.
    This function expects a dictionary of values (Which is the default return value from SQL for retrieving a single listing.), and a boolean value for is_owner.
    :model:`auctions.models.Listing`.
    """
    if error:
        return render(
            request,
            "auctions/getListing.html",
            {
                "Listing_id": valuesDict["listing_id"],
                "Listing_name": valuesDict["listing_name"],
                "Listing_description": valuesDict["listing_description"],
                "Listing_category": valuesDict["listing_category"],
                "Listing_status": valuesDict["listing_status"],
                "Listing_startTime": valuesDict["listing_start_time"],
                "Listing_endTime": valuesDict["listing_end_time"],
                "Listing_duration": valuesDict["listing_duration"],
                "Listing_image": valuesDict["listing_image"],
                "bids": bidsDict,
                "comments": commentsDict,
                "WatchlistForm": WatchlistForm(),
                "CommentForm": CommentForm(),
                "BidForm": BidForm(),
                "is_owner": is_owner,
                "error": error,
            },
        )
    return render(
        request,
        "auctions/getListing.html",
        {
            "Listing_id": valuesDict["listing_id"],
            "Listing_name": valuesDict["listing_name"],
            "Listing_description": valuesDict["listing_description"],
            "Listing_category": valuesDict["listing_category"],
            "Listing_status": valuesDict["listing_status"],
            "Listing_startTime": valuesDict["listing_start_time"],
            "Listing_endTime": valuesDict["listing_end_time"],
            "Listing_duration": valuesDict["listing_duration"],
            "Listing_image": valuesDict["listing_image"],
            "bids": bidsDict,
            "comments": commentsDict,
            "WatchlistForm": WatchlistForm(),
            "CommentForm": CommentForm(),
            "BidForm": BidForm(),
            "is_owner": is_owner,
        },
    )


def postForm(request, formString: str):
    """
    The logic that takes a form's data, validates it, and also saves the cleaned data to it's appropriate SQLite table.
    If successful, you will be redirected.
    :model:`auctions.models`,
    """
    if request.method == "POST":
        if request.FILES:
            form = f"{formString}Form"(request.POST, request.FILES)
        else:
            form = f"{formString}Form"(request.POST)
        if form.is_valid():
                # Save valid listing request
                f"{formString}".save(form.cleaned_data)

                # Redirect user to list of entries
                return HttpResponseRedirect(reverse("index"))
