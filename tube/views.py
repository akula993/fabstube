from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tube.models import Channel


class HomeView(ListView):
    model = Channel
    template_name = 'tube/index.html'
    context_object_name = 'channels'


class AccountView(DetailView):
    model = Channel
    template_name = 'tube/account.html'
    context_object_name = 'accout'
