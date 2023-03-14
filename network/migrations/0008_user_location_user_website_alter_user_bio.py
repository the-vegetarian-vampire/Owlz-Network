# Generated by Django 4.1.4 on 2023-03-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_rename_post_comment_post_comment_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]