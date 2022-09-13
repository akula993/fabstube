from django.urls import path

from tube.views import AccountView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('account/<slug:slug>', AccountView.as_view(), name='account'),
]
