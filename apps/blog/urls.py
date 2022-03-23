from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    path('video_juegos/', video_juegos, name='video_juegos'),
    path('<slug:slug>/', detalle_post, name='detalle_post'),
]