from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/create", views.create_listing, name="createListing"),
    path("listing/close/", views.close_listing, name="closeListing"),
    path("listing/get/<str:id>", views.get_listing, name="getListing"),
    path(
        "comment/add/<str:id>/<str:user_id>", views.create_comment, name="createComment"
    ),
    path("bid/add/<str:id>/<str:user_id>", views.bid_on_listing, name="bidOnListing"),
    path("watchlist/add/<str:id>", views.add_to_watchlist, name="addToWatchList"),
]
