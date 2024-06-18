# Requirements gathering

## Pages:
- Create Listing / Create Route
- Active Listings / Get all listings
    - If a user is signed in user should be able to add an item to their request.session['watchlist'](which should have its own page that leads back to the listing page itself.) variable. - If it's already in the watch list it this should remove it.
    - If user is signed in user should be able to bid on an item. The bid must be at least as large as the starting bid and greater than any other bids that have been placed thus far. If - criteria not met, user will see error page.
    - If user is signed in and has any created listings they should be able to close the listing page and make the highest bidder the winner.
    = If a user is signed into a closed list that a user has won, the page should alert said user.
- Users should have a category list available to use to filter through listings. Clicking on a listing name should take the user to that page of listings.

- Remember to add Ruff linter to project. Will detail steps and which settings should be used. Will pre-config pre-commit hook as well.

## Required models:
- Auction/Listings, Bids, Comments

```
Bids:
    bid id, type:guid
    bid placed, type:datetime, default=datetime.now
    bid amount, type:int
    bid owner, type:string

Comments:
    comment id, type:guid
    comment owner username, type:string
    comment content, type:string
    comment datetime comment made, type:datetime, default=datetime.now
    comment reaction, type:string

Listing:
    listing id, type:guid
    listed product name, type:string
    listed product description, type:string,
    listing type, type:list, default=['single','multiples']
    listing duration, type:time,
    listing starttime, type:datetime, default=datetime.now
    listing endtime, type: datetime, 
    listing reaction, type:string
   
Reaction:
    reaction id, type:guid
    reaction data, type:string

Rating:
    rating id, type:guid
    rating data, type:integer
```

## Pub/Sub Events Based on Topics:
Highest biddest
New Bid
New Listing in Favorite Category
Listing Started
Listing Closed
Won Listing
Lost Listing
