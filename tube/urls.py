from django.urls import path

from tube.views import HomeView, VideoView, VideoCreate, VideoUpdate

urlpatterns = [
    path('video/create/', VideoCreate.as_view(), name='video_create_url'),
    path('video/create/<int:pk>/', VideoUpdate.as_view(), name='video_update'),
    path('stream/<int:pk>/', VideoView.get_streaming_video, name='stream'),
    path('', HomeView.as_view(), name='home'),
]
