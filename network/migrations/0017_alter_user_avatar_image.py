# Generated by Django 4.1.4 on 2023-03-10 17:29

from django.db import migrations, models
import network.models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_alter_user_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_image',
            field=models.ImageField(default='static/network/images/owl-silhouette.png', upload_to=network.models.avatar_upload),
        ),
    ]
