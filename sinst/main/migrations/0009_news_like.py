# Generated by Django 5.0.6 on 2024-07-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_like_news_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]