from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}, {self.date}, {self.user}, {self.photo}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class News_Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_liked = models.BooleanField(default=False)
    likes = models.IntegerField(default=0, blank=True, null=True)


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(News, on_delete=models.CASCADE, related_name='text')
    photo = models.ForeignKey(News, on_delete=models.CASCADE, related_name='image')
    date = models.ForeignKey(News, on_delete=models.CASCADE, related_name='created_at')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    likes = models.ForeignKey(News_Like, on_delete=models.CASCADE, related_name='likes_count', blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
