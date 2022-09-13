from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from tube.models import Channel
from tube.services import open_file


class VideoView:
    def get_streaming_video(request, pk: int):
        file, status_code, content_length, content_range = open_file(request, pk)
        response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(content_length)
        response['Cache-Control'] = 'no-cache'
        response['Content-Range'] = content_range
        return response


class HomeView(ListView):
    model = Channel
    template_name = 'tube/index.html'
    context_object_name = 'channels'


class AccountView(DetailView):
    model = Channel
    template_name = 'tube/account.html'
    context_object_name = 'account'
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
