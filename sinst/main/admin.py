from django.contrib import admin

from .models import News, Users, News_Like, Comment

admin.site.register(News)
admin.site.register(Users)
admin.site.register(News_Like)
admin.site.register(Comment)



