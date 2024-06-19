from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Bid, Listing, Comments

class CreateListingForm(forms.Form):
    listing_name = forms.CharField(label="Listing Product", max_length=90, required=True)
    listing_description = forms.Textarea()
    listing_category = forms.CharField(label="Listing Category", max_length=90, required=True)
    listing_status = forms.CharField(initial="Active", disabled=True)
    listing_start_time = forms.DateTimeField(initial=datetime.now())
    listing_duration = forms.TimeField(label="Duration of Listing", required=True, disabled=True)


def index(request):
    return render(request, "auctions/index.html")


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

#Create listing view to display proper information.
def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/createListing.html", {
            "createListingForm": CreateListingForm()
        })
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        listing = {}
        if form.is_valid():
            
            #Save valid listing request
            Listing.save(form.cleaned_data)

            # Redirect user to list of entries
            return HttpResponseRedirect(reverse("index"))