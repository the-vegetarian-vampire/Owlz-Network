from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
import json

from .models import User, Post, Followers


def index(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        content = request.POST["content"]
        Post.objects.create(content=content, author=request.user)
        return HttpResponseRedirect(reverse("index"))
    else:
        all_posts = Post.objects.all().order_by("-time")
        paginator = Paginator(all_posts, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        return render(request, "network/index.html", {
            "page": page
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def following(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = User.objects.get(id=request.user.id)
    followed_users = [followRelation.user for followRelation in user.following.all()]
    posts = Post.objects.filter(author_id__in=followed_users).order_by("-time")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "page": page,
        "followed_users": followed_users
})

def profile(request):
    return render(request, "network/profile.html")

def edit_hoot(request):
    return render(request, "network/index.html")
