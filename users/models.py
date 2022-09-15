from urllib import request

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    pass



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(max_length=500, blank=True, verbose_name="Описание канала")
    location = models.CharField(max_length=30, blank=True, verbose_name='Размишение')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата создания канала', auto_now_add=True)
    image = models.ImageField(verbose_name='Фото профиля', upload_to='photo_users', blank=True, null=True)
    slug = models.SlugField(unique=True,blank=True, null=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Подробнее о пользователе'
        verbose_name_plural='Подробнее о пользователях'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse('users:profile', kwargs={'user': self.user.username})

#

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()