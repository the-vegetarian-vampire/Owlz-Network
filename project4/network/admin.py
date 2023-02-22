from django.contrib import admin
from .models import User, Post, Followers

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")

class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "time",)

class FollowersAdmin(admin.ModelAdmin):
    list_display = ("user", "follower")

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Followers, FollowersAdmin)
