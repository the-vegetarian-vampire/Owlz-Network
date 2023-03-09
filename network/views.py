from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .forms import UserForm
from django.shortcuts import get_object_or_404, render, resolve_url
import json
import random

from .models import User, Post, Followers, Comment


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

        # Get Random User per Layout HTML
        all_profiles = User.objects.all()
        random_profile = random.choice(all_profiles)
        # All Users
        all_users = User.objects.all().count()
        """
        # remove bookmark
        data = Post.objects.get(pk=id)
        user = request.user
        remove_bookmark = data.bookmarked_by.remove(user)
        # add bookmark
        add_bookmark = data.bookmarked_by.add(user)
        user = User.objects.get(username=request.user)
        avatar_image = User.objects.filter(user=user)
        # all comments
        data = Post.objects.get(pk=id)
        all_comments = Comment.objects..all()
        total_comments = all_comments.count()
        """
        return render(request, "network/index.html", {
            "all_posts": all_posts,
            "page_posts": page_posts,
            "random_profile": random_profile,
            "all_profiles": all_profiles,
            "all_users": all_users,
            # "all_comments": all_comments,
            # "total_comments": total_comments,
            # "remove_bookmark": remove_bookmark,
            # "add_bookmark": add_bookmark,
            # "avatar_image": avatar_image,
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
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
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
            user.first_name = first_name
            user.last_name = last_name
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
    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)
    # All Users
    all_users = User.objects.all().count()
    return render(request, "network/following.html", {
        "page_posts": page_posts,
        "followed_users": followed_users,
        "all_profiles": all_profiles,
        "random_profile": random_profile,
        "all_users": all_users,
})
 
@login_required
def profile(request, username):
    user_profile = User.objects.get(username=username)
    if request.method == "POST":
        if "profile_submit_button" in request.POST:
            new_bio = request.POST["Biography"]
            new_location = request.POST["home"]
            new_website = request.POST["url_site"]
            new_dob = request.POST["birth"]
            request.user.bio = new_bio
            request.user.location = new_location
            request.user.website = new_website
            request.user.dob = new_dob
            request.user.save()
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        if "delete_button" in request.POST:
            return HttpResponseRedirect(reverse("profile", args=(username, )))
        if "unfollow_button" in request.POST:
            Followers.objects.get(user=user_profile, follower=request.user).delete()
        elif "follow_button" in request.POST:
            Followers.objects.create(user=user_profile, follower=request.user)
        else:
            return HttpResponseRedirect(reverse("profile", args=(username, )))

    user_follows_profile = False
    if request.user.is_authenticated:
        user_follows_profile = request.user.following.filter(user=user_profile.id).exists()
    user_posts = user_profile.posts.order_by("-time").all()
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    # Show All Followers and All Following
    show_all_followers = user_profile.followers.all()
    show_all_following = user_profile.following.all()
    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)
    # Show Bookmarks
    # user = request.user
    # bookmarks = user.bookmarks.all().order_by("-time")
    bio = user_profile.bio
    location = user_profile.location
    website = user_profile.website
    dob = user_profile.dob
    # All Users
    all_users = User.objects.all().count()
    return render(request, "network/profile.html", {
        "user_profile": user_profile,
        "user_posts": user_profile.posts.order_by("-time").all(),
        "page_posts": page_posts,
        "following_profile": user_follows_profile,
        "show_all_followers": show_all_followers,
        "show_all_following": show_all_following,
        "all_profiles": all_profiles,
        "random_profile": random_profile,
        "bio": bio,
        "location": location,
        "website": website,
        "dob": dob,
        "all_users": all_users,
        #"bookmarks": bookmarks,
        
    })

@csrf_exempt
@login_required
def edit_hoot(request):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    data = json.loads(request.body)
    post_id = data.get("post_id", "")
    time = data.get("time", "")
    post = Post.objects.get(id=post_id)
    # time = post.get.time
    content = data.get("content", "")
    if content:
        if request.user != post.author:
            return JsonResponse({"error": "Can only edit your posts"})
        if len(content) > 280:
            return JsonResponse({"error": "Too many Characters"})
        post.content = content
    post.save()
    return JsonResponse({"message": "Post edited", "content": str(content)}, status=201)

@csrf_exempt
@login_required
def like_post(request, post_id):
    user = request.user
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error in views.py"}, status=404)
    # If the user liked the post, unlike it
    if (user.likes.filter(pk=post_id).exists()):
        post.liked_by.remove(user)
        likes_post = False
    else: 
        post.liked_by.add(user)
        likes_post = True
    # Update num of likes on post
    likes = post.likes()
    return JsonResponse({"likesPost": likes_post, "likesCount": likes}, status=200)

@login_required
def bookmarks(request):
    if request.method == "GET":
        bookmarks = Post.objects.all()
        return render(request, "network/bookmarks.html", {
            "bookmarks": bookmarks,
            })

@login_required
def remove_bookmarks(request, id):
    user = request.user
    data = Post.objects.get(pk=id)
    update_bookmarks = data.bookmarked_by.remove(user)
    try:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', update_bookmarks))
    finally:
        return HttpResponseRedirect(reverse("index", update_bookmarks))

@login_required
def add_bookmarks(request, id):
    data = Post.objects.get(pk=id)
    user = request.user
    update_bookmarks = data.bookmarked_by.add(user)
    try:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', update_bookmarks))
    finally:
        return HttpResponseRedirect(reverse("index", update_bookmarks))

@login_required
def display_bookmarks(request):
    user = request.user
    bookmarks = user.bookmarks.all().order_by("-time")
    paginator = Paginator(bookmarks, 10)
    page_number = request.GET.get('page', 1)
    page_posts = paginator.get_page(page_number)
    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)
    # All Users
    all_users = User.objects.all().count()
    return render(request, "network/bookmarks.html", {
        "bookmarks": bookmarks,
        "paginator": paginator,
        "page_number": page_number,
        "page_posts": page_posts,
        "all_profiles": all_profiles,
        "random_profile": random_profile,
        "all_users": all_users,
    })

@login_required
def inbox_messages(request):
    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)
     # All Users
    all_users = User.objects.all().count()
    return render(request, "network/messages.html", {
        "all_profiles": all_profiles,
        "random_profile": random_profile,
        "all_users": all_users,
    })


def search_results(request, *args, **kwargs):
    context = {}
    if request.method == "GET":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            search_results = User.objects.filter(username__icontains=search_query) or User.objects.filter(first_name__icontains=search_query) # .distinct()  # distinct() operator eliminates duplicate results 
            accounts = []
            for account in search_results:
                accounts.append((account))
            context['accounts'] = accounts
            print("\n" f"{accounts}" "\n")

    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)
    # All Users
    all_users = User.objects.all().count()

    return render(request, "network/search_results.html", {
        "context": context,
        "accounts": accounts,
        "search_query": search_query,
        "random_profile": random_profile,
        "all_users": all_users,
    }) 

@login_required
def comments(request, id):
    user = request.user
    original_post = Comment.objects.get(pk=id)
    new_comment = request.POST['new_comment']
    new_comment = Comment(
        original_post=original_post,
        comment_author=user, 
        new_comment=new_comment
    )
    new_comment.save()
    return HttpResponseRedirect(reverse("comments",args=(id, )))
"""

""" 
@login_required
def delete_post(request, post_id):
    if request.user.is_authenticated and "delete_button" in request.POST:
        delete_post = Post.objects.get(pk=post_id).delete()
    # return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect(reverse("index", delete_post))
