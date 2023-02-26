from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    bookmarked_by = models.ManyToManyField(User, blank=True, null=True, related_name="bookmarks")
    content = models.CharField(max_length=10000)
    liked_by = models.ManyToManyField(User, blank=True, related_name="likes")
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} posted {self.content}"

    def likes(self):
        return self.liked_by.all().count()

    def bookmarks(self):
        return self.bookmarked_by.all().count()

class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return f"{self.follower} follows {self.user}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="post_comment")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="comment_author")
    message = models.CharField(max_length=280)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_author} commented on {self.post}"