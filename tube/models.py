from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.urls import reverse

from users.models import User, Profile


class Video(models.Model):
    slug = models.SlugField(max_length=150, verbose_name='Название')
    file = models.FileField(upload_to='video', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    view = models.IntegerField(verbose_name='Кол-во просмтортров', default=0, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.file)
        # self.profile = Profile.user
        super(Video, self).save(*args, **kwargs)


    # def render_video(self, **kwargs):
    #     poster_markup = '<img src="%s" height="%d" width="%d" />' %
    #     return super(TestVideo, self).render_video(
    #         poster_markup=poster_markup)
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('upload', args=[str(self.id)])
