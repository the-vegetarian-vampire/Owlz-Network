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
    return render(request, "network/following.html", {
        "page_posts": page_posts,
        "followed_users": followed_users,
        "all_profiles": all_profiles,
        "random_profile": random_profile,
})

@login_required
def profile(request, username):
    user_profile = User.objects.get(username=username)
    bio = user_profile.bio
    dob = user_profile.dob
    location = user_profile.location
    website = user_profile.website

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
    # Show Bookmarks
    # user = request.user
    # bookmarks = user.bookmarks.all().order_by("-time")
    # Show All Followers and All Following
    show_all_followers = user_profile.followers.all()
    show_all_following = user_profile.following.all()
    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)

    # User Bio
    # user_bio = request.POST["bio"]
    # bio = User.objects.create(user_bio=user_bio, User=request.user)

    return render(request, "network/profile.html", {
        "user_profile": user_profile,
        "bio": bio,
        "dob": dob,
        "location": location,
        "website": website,
        "user_posts": user_profile.posts.order_by("-time").all(),
        "page_posts": page_posts,
        "following_profile": curr_user_follows_this_profile,
        "show_all_followers": show_all_followers,
        "show_all_following": show_all_following,
        "all_profiles": all_profiles,
        "random_profile": random_profile,

        # "bio": bio,
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
    post = Post.objects.get(id=post_id)
    content = data.get("content", "")
    post.save()
    return JsonResponse({"message": "Post edited successfully", "content": str(content)}, status=201)


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
    data.bookmarked_by.remove(user)
    return HttpResponseRedirect(reverse("index"))

@login_required
def add_bookmarks(request, id):
    data = Post.objects.get(pk=id)
    user = request.user
    update_bookmarks = data.bookmarked_by.add(user)
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
    return render(request, "network/bookmarks.html", {
        "bookmarks": bookmarks,
        "paginator": paginator,
        "page_number": page_number,
        "page_posts": page_posts,
        "all_profiles": all_profiles,
        "random_profile": random_profile,
    })

@login_required
def inbox_messages(request):
    # Get Random User per Layout HTML
    all_profiles = User.objects.all()
    random_profile = random.choice(all_profiles)
    return render(request, "network/messages.html", {
        "all_profiles": all_profiles,
        "random_profile": random_profile,
    })

"""
def search(request):
    if request.method == "POST":
        entry = request.POST['q']
        search_name = ...(entry)
        if search_name != None:
            return render(request, "/.html", {
            "title": entry,
            "content": search_name
            })
        else:
            list = []
            entries = util.list_entries()
            for item in entries:
                if entry.lower() in item.lower():
                    list.append(item)
            return render(request, "/.html", {
                "list": list
                })

                search_input = self.request.GET.get('search-area') or ''
                if search_input:
                    ['users']
"""

def add_comment(request, id):
    user = request.user
    post_comment = Post.objects.get(pk=id)
    message = request.POST['new_comment']

    new_comment = Comment(
        author=user, 
        post_comment=post_comment,
        message=message
    )
    new_comment.save()
    return HttpResponseRedirect(reverse("index",args=(id, )))

def delete_post(request, post_id):
    delete_post= Post.objects.get(pk=post_id).delete()
    return render(request, "network/index.html", {
        "delete_post": delete_post,
    })
   