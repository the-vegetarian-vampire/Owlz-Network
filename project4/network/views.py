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
        page_posts = paginator.get_page(page_number)
        return render(request, "network/index.html", {
            "all_posts": all_posts,
            "page_posts": page_posts
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
    page_posts = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "page_posts": page_posts,
        "followed_users": followed_users
})

def profile(request, username):
    user_profile = User.objects.get(username=username)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        if "unfollow_button" in request.POST:
            Followers.objects.get(user=user_profile, follower=request.user).delete()
        elif "follow_button" in request.POST:
            Followers.objects.create(user=user_profile, follower=request.user)
        else:
            pass
        return HttpResponseRedirect(reverse("profile", args=(username, )))

    curr_user_follows_this_profile = False
    if request.user.is_authenticated:
        curr_user_follows_this_profile = request.user.following.filter(user=user_profile.id).exists()

    user_posts = user_profile.posts.order_by("-time").all()
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, "network/profile.html", {
        "user_profile": user_profile,
        "user_posts": user_profile.posts.order_by("-time").all(),
        "page_posts": page_posts,
        "following_profile": curr_user_follows_this_profile
    })

def edit_hoot(request, post_id):
    if request.method != "POST":
        return JsonResponse({"Request error, 404"}, status=400)
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist:
        return JsonResponse({"Request error, 404"}, status=404)
    if request.user == post.author:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['content']
        Post.objects.filter(pk=post_id).update(content=f'{content}')

        # Returns Json Response with content passed back that we can use with JS to update page
        return JsonResponse({"message": "Post updated successfully.", "content": content}, status=200)

    else:
        return JsonResponse({"error": "You do not have permission to do this"}, status=400)

