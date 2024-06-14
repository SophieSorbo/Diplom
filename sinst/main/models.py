from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}, {self.date}, {self.user}, {self.photo}, {self.comments}, {self.likes}'

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Likes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'{self.user}, {self.news}'

class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.user}, {self.news}, {self.text}, {self.date}'