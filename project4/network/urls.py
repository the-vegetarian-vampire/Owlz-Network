
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_bookmarks/<int:id>", views.add_bookmarks, name="add_bookmarks"),
    path("comments/<int:id>", views.comments, name="comments"),
    path("bookmarks", views.display_bookmarks, name="display_bookmarks"),
    path("edit_hoot", views.edit_hoot, name="edit_hoot"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
    path("following", views.following, name="following"),
    path("likepost/<int:post_id>", views.like_post, name = "like_post"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("messages", views.inbox_messages, name="messages"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("register", views.register, name="register"),
    path("remove_bookmarks/<int:id>", views.remove_bookmarks, name="remove_bookmarks"),
    
    # path('search/', views.search, name="search"),
   
]
