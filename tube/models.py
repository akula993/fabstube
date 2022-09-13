from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from users.models import User


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(max_length=150)
    view = models.IntegerField(verbose_name='Кол-во просмтортров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Language(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(max_length=150)
    view = models.IntegerField(verbose_name='Кол-во просмтортров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Tag(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(max_length=150)
    view = models.IntegerField(verbose_name='Кол-во просмтортров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Channel(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    about = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

    def get_absolute_url(self):
        return reverse('account', kwargs={'slug': self.user})

class Playlist(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название плейлиста')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='playlist', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'


class Video(models.Model):
    slug = models.SlugField(max_length=150)
    file = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    about = models.TextField(verbose_name='Описание', blank=True, null=True)
    language_in_video = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='language', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    view = models.IntegerField(verbose_name='Кол-во просмтортров', default=0, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tag', blank=True, null=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


