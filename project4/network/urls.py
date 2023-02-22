
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edithoot/<int:post_id>", views.edit_hoot, name="edit"),
    path("following", views.following, name="following"),
    path("likepost/<int:post_id>", views.like_post, name = "like_post"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("register", views.register, name="register"),
   
]
