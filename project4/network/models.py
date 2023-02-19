from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=10000)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} posted {self.content}"

    def likes(self):
        return self.likes.all().count()

class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return f"{self.user} is following {self.follower}"
