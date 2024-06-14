from django.contrib import admin

from .models import News, Likes, Comments

admin.site.register(News)
admin.site.register(Likes)
admin.site.register(Comments)

