from django.contrib import admin
from .models import User, Post, Followers, Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "bio", "dob", "location", "website")
    search_fields = ('avatar','username','first_name','last_name')

class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "time", "likes", "bookmarks")

class FollowersAdmin(admin.ModelAdmin):
    list_display = ("user", "follower")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("original_post", "new_comment", "comment_author", "time")

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Followers, FollowersAdmin)
admin.site.register(Comment, CommentAdmin) 