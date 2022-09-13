from django.urls import path

from tube.views import AccountView

urlpatterns = [
    path('account/<slug:slug>', AccountView.as_view(), name='account')
]
