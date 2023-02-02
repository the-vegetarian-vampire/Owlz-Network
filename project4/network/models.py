from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    following = models.ManyToManyField("self", blank=True, related_name='followers', symmetrical=False)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=10000)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    time = models.DateTimeField(auto_now=True)




