from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.abstractions import postForm, returnBidResponse, returnGetListing
from auctions.validators import validate_bid

from .forms import BidForm, CommentForm, CreateListingForm, WatchlistForm
from .models import Bid, Comments, Listing, User, Watchlist


# Base route when you first login.
@login_required(login_url='/login')
def index(request):
    indexURI = "auctions/index.html"
    all_listings = Listing.objects.values().all()
    print(all_listings)
    return render(
            request,
            indexURI,
            {
                "all_listings": all_listings,
                "user_id": request.user.user_id,
                "WatchlistForm": WatchlistForm(),
    })


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

#Logout view
@login_required(login_url='/login')
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
@login_required(login_url='/login')
def create_listing(request):
    """
    Create an individual :model:`auctions.Listing`.

    **Template:**

    :template:`auctions/createListing.html`
    """
    indexURI = "auctions/index.html"
    if request.method == "GET":
        return render(
            request,
            "auctions/createListing.html",
            {"createListingForm": CreateListingForm()},
        )
    if request.method == "POST":
        form = CreateListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.listing_owner_id_id = request.user.user_id
            # Save valid listing request
            listing.save()
            
            all_listings = Listing.objects.values().all()
            # Redirect user to list of entries
            return render(
            request,
            indexURI,
            {
                "user_id": request.user.user_id,
                "WatchlistForm": WatchlistForm(),
            })
        else:
            return HttpResponseRedirect(reverse("index"))

# Return categories route.
@login_required(login_url='/login')
def return_category(request, category):
    indexURI = "auctions/index.html"
    listings = Listing.objects.filter(listing_category=category).values()
    return render(
        request,
        indexURI,
        {
            "all_listings": listings,
            "user_id": request.user.user_id,
            "WatchlistForm": WatchlistForm(),
        },
    )

#Create comment route.
@login_required(login_url='/login')
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
@login_required(login_url='/login')
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
        commentsDict = (
            Comments.objects.filter(listing_id=id).order_by("-comment_id").values()
        )
        bidsDict = Bid.objects.filter(listing_id=id).order_by("-bid_amount").values()
        Listing_owner = valuesDict["listing_owner_id_id"]
        is_owner = False
        if Listing_owner == request.user.user_id:
            is_owner = True
            error = None
            return returnGetListing(
                request, valuesDict, is_owner, commentsDict, bidsDict, error
            )
        else:
            error = None
            return returnGetListing(
                request, valuesDict, commentsDict, bidsDict, is_owner, error
            )

# Close a listing post route.
@login_required(login_url='/login')
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

# Add a listing to watchlist post route.
@login_required(login_url='/login')
def add_to_watchlist(request, id, user_id):
    if request.method == "POST":
        form = WatchlistForm(request.POST)
        user = User.objects.get(user_id=user_id)
        listing = Listing.objects.get(listing_id=id)
        if form.is_valid():
            print(form.cleaned_data)
            watchlistItem = Watchlist(
                add_to_list=form.cleaned_data["add_to_list"],
                user_id=user,
                listing_id=listing,
            )
            Watchlist.save(watchlistItem)
            return HttpResponseRedirect(reverse("index"))
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))

# Bid on a listing post route.
@login_required(login_url='/login')
def bid_on_listing(request, id, user_id):
    if request.method == "POST":
        listing = Listing.objects.get(listing_id=id)
        commentsDict = Comments.objects.filter(listing_id=id).values()
        bidsDict = (
            Bid.objects.filter(listing_id=id).values().order_by("-bid_amount").values()
        )
        Listing_owner = listing.listing_owner_id_id
        form = BidForm(request.POST)
        if form.is_valid():
            bidsDict = Bid.objects.filter(listing_id=id).values()
            bid_amount = bidsDict[0]["bid_amount"]
            validated_value = validate_bid(form.cleaned_data["bid_amount"], bid_amount)
            if validated_value is False:
                is_owner = False
                if Listing_owner == request.user.user_id:
                    is_owner = True
                return returnBidResponse(
                    request,
                    valuesDict=listing,
                    is_owner=is_owner,
                    bidsDict=bidsDict,
                    commentsDict=commentsDict,
                    error="Your bid was too low. Please make a higher bid.",
                )
            user = User.objects.get(user_id=user_id)
            bid = Bid(bid_amount=validated_value, listing_id=listing, user_id=user)
            Bid.save(bid)
            is_owner = False
            if Listing_owner == request.user.user_id:
                is_owner = True
                bidsDict = (
                    Bid.objects.filter(listing_id=id).order_by("-bid_amount").values()
                )
            return returnBidResponse(
                request,
                valuesDict=listing,
                is_owner=is_owner,
                bidsDict=bidsDict,
                commentsDict=commentsDict,
                error=None,
            )
        else:
            return HttpResponseRedirect(reverse("index"))

# Bid on a listing post route.
@login_required(login_url='/login')
def get_watch_list(request):
    if request.method == "GET":
        watchlist = Watchlist.objects.filter(user_id_id=request.user.user_id).values()
        return render(request, "auctions/watchlist.html", {
            "watchlist": watchlist,
        })