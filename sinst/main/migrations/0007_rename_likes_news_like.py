# Generated by Django 5.0.6 on 2024-07-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_news_comments_news_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='likes',
            new_name='like',
        ),
    ]