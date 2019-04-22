"""online_lgms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('lgmssis/', include('lgmssis.urls')),
    path('', RedirectView.as_view(url='/lgmssis/', permanent=True)),
    path('pages/', include('django.contrib.flatpages.urls')),

    #path('accounts/login/', auth_views.LoginView.as_view(template_name='lgmssis/login.html')),

    #this is for the flatpages
    path('home/', views.flatpage, {'url': '/home/'}, name='home'),
    path('aboutus/', views.flatpage, {'url': '/about/'}, name='about'),
    path('gallery/', views.flatpage, {'url': '/gallery/'}, name='gallery'),
    path('contact/', views.flatpage, {'url': '/contact/'}, name='contact'),
    path('news/', views.flatpage, {'url': '/news/'}, name='news'),
    path('faq1/', views.flatpage, {'url': '/faq1/'}, name='faq1'),
    path('faq2/', views.flatpage, {'url': '/faq2/'}, name='faq2'),
    path('coming-soon/', views.flatpage, {'url': '/coming-soon/'}, name='coming-soon'),
    path('privacy/', views.flatpage, {'url': '/privacy/'}, name='privacy'),
    path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),

    #accounts management


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
