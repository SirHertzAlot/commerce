from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.abstractions import postForm, returnGetListing

from .forms import BidForm, CommentForm, CreateListingForm
from .models import Bid, Comments, Listing, User, Watchlist


def index(request):
    all_listings = Listing.objects.values().all()
    return render(request, "auctions/index.html", {"all_listings": all_listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# Create listing view to display proper information.
def create_listing(request):
    """
    Create an individual :model:`auctions.Listingmodel`.

    **Template:**

    :template:`auctions/createListing.html`
    """
    if request.method == "GET":
        return render(
            request,
            "auctions/createListing.html",
            {"createListingForm": CreateListingForm()},
        )
    if request.method == "POST":
        return postForm(request, "Listing")


def create_comment(request, id, user_id):
    """
    Create an individual :model:`auctions.Commentss`.

    :template:`auctions/getListing.html`
    """
    if request.method == "POST":
        user = User.objects.get(user_id=user_id)
        listing = Listing.objects.get(listing_id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                Comment=form.cleaned_data["Comment"],
                comment_owner_id=user,
                listing_id=listing,
            )
            Comments.save(comment)
            return HttpResponseRedirect(reverse("index"))


# Get listing based off of listing id
def get_listing(request, id):
    """
    Display an individual :model:`auctions.Listing` model.

    **Context**

    ``Listing``
        An id of :model:`auctions.Listingmodel`.

    **Template:**

    :template:`auctions/getListing.html`

    **Input:**
    :input:`an ID`
    """
    if request.method == "GET":
        valuesList = Listing.objects.filter(pk=id).values()
        valuesDict = valuesList[0]
        commentsDict = Comments.objects.filter(listing_id=id).values()
        bidsDict = Bid.objects.filter(listing_id=id).values()
        Listing_owner = valuesDict["listing_owner_id_id"]
        is_owner = False
        if Listing_owner == request.user.user_id:
            is_owner = True
            return returnGetListing(
                request, valuesDict, is_owner, commentsDict, bidsDict
            )
        else:
            return returnGetListing(request, valuesDict, is_owner)


def close_listing(request):
    """
    Change the status of a listing to closed. :model:`auctions.Listing.listing_status` model.

    **Context**

    ``Listing``
        An id of :model:`auctions.Listingmodel.listing_id`.

    **Template:**

    :template:`auctions/getListing.html`

    **Input:**
    :input:`an ID`
    """
    return postForm(request, "Listing")


def add_to_watchlist(request):
    return postForm(request, "Watchlist")


def bid_on_listing(request, id, user_id):
    if request.method == "POST":
        user = User.objects.get(user_id=user_id)
        listing = Listing.objects.get(listing_id=id)
        form = BidForm(request.POST)
        if form.is_valid():
            bid = Bid(
                bid_amount=form.cleaned_data["bid_amount"],
                user_id=user,
                listing_id=listing,
            )
            Bid.save(bid)
            return HttpResponseRedirect(reverse("index"))
