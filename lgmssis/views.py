from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic

def indexpage(request):
    return render(request, 'lgmssis/index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class Apply(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy ('login')
    template_name = 'registration/apply-online.html'
