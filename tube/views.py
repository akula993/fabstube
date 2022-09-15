from django.core.files.storage import FileSystemStorage
from django.http import StreamingHttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from tube.forms import VideoForm, VideoUpdateForm
from tube.models import Video
from tube.services import open_file
from users import models
from users.models import Profile


class HomeView(ListView):
    model = models.Profile
    template_name = 'apps/tube/index.html'
    context_object_name = 'profile'
    slug_field = 'username'


class VideoView:
    def get_streaming_video(request, pk: int):
        file, status_code, content_length, content_range = open_file(request, pk)
        response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(content_length)
        response['Cache-Control'] = 'no-cache'
        response['Content-Range'] = content_range
        return response


class VideoCreate(CreateView):
    """Добовление видео"""
    model = Video
    template_name = 'apps/tube/upload.html'
    form_class = VideoForm
    success_url = '/'





class VideoUpdate(UpdateView):
    model = Video
    template_name = 'apps/tube/uploadvideo.html'
    form_class = VideoUpdateForm
    extra_context = {'video': Video.objects.all()}
    success_url = '/'


class VideoDetail(DetailView):
    model = Video
    template_name = 'apps/tube/video-page.html'
    context_object_name = 'video'

    #
    # def get_context_data(self, *args, **kwargs):
    #     users = Channel.objects.all()
    #     context = super(AccountView, self).get_context_data(*args, **kwargs)
    #     page_user = get_object_or_404(Channel, id=self.kwargs['pk'])
    #     context['page_user'] = page_user
    #     return context

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.views += 1
    #     self.object.save()
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)
