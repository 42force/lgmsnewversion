from django.urls import path
#from lgmssis.views import MyView
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.indexpage, name='indexpage'),

    #path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('hello/', MyView.as_view(), name='my-view'),
]
