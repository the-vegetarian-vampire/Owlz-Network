
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bookmarks/<int:post_id>", views.bookmarks, name="bookmarks"),
    path("remove_bookmarks/<int:id>", views.remove_bookmarks, name="remove_bookmarks"),
    path("add_bookmarks/<int:id>", views.add_bookmarks, name="add_bookmarks"),
    path("display_bookmarks", views.display_bookmarks, name="display_bookmarks"),
    path("edithoot/<int:post_id>", views.edit_hoot, name="edit"),
    path("following", views.following, name="following"),
    path("messages", views.inbox_messages, name="messages"),
    path("likepost/<int:post_id>", views.like_post, name = "like_post"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("register", views.register, name="register"),
   
]
