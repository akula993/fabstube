from django.core.exceptions import ValidationError
from django.forms import Form
from django.template.defaultfilters import slugify

from users.models import User, Profile
from .models import Video
# from django.forms import ModelForm
from django import forms


class VideoForm(forms.ModelForm):
    # form = VideoForm(initial={'profile': User})
    class Meta:
        model = Video

        fields = ['file', 'slug', 'profile']


class VideoUpdateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
