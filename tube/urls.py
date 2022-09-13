from django.urls import path

from tube.views import AccountView, HomeView, VideoView

urlpatterns = [
    path('stream/<int:pk>/', VideoView.get_streaming_video, name='stream'),
    path('', HomeView.as_view(), name='home'),
    path('accounts/profile/<int:pk>/', AccountView.as_view(), name='profile')
]
