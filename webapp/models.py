from django.db import models
from django.contrib.auth import get_user_model


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures', verbose_name='Фото')
    caption = models.CharField(max_length=100, verbose_name='Подпись')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время-создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', null=True, blank=True, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite_pics', null=True, blank=True)

    def __str__(self):
        return self.caption


class Album(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание', blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время-создания')
    private = models.BooleanField(default=False)
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite_albums', null=True, blank=True)

    def __str__(self):
        return self.name
