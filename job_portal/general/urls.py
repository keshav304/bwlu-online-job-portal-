
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('login', views.login, name='login'),
    path('seeker', views.Seeker, name='seeker'),
    path('recruiter', views.Recruiter, name='recruiter'),
    path('home-recruiter', include('recruiter.urls')),
    path('home-seeker', include('seeker.urls'))
]
