from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


    def __str__(self):
        return f'{self.user}'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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




class News_Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_liked = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.news}, {self.user}, {self.is_liked}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.news}, {self.user}, {self.comment}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
