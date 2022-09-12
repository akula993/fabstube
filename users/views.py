from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)