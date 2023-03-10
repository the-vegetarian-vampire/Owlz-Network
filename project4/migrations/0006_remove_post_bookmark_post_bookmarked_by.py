# Generated by Django 4.1.4 on 2023-02-24 19:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_post_bookmark_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bookmark',
        ),
        migrations.AddField(
            model_name='post',
            name='bookmarked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]