from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


def courselist(request):
    return render(request, 'lgmssis/course-listing.html')

def index(request):
    return render(request, 'lgmssis/index.html')
