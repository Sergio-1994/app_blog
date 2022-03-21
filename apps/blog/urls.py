from django.urls import path
from .views import home, generales, programacion, video_juegos, tecnologia, tutoriales

urlpatterns = [
    path('', home, name = 'index'),
    path('generales/', generales, name = 'generales'),
    path('programacion/', programacion, name = 'programacion'),
    path('video_juegos/', video_juegos, name = 'video_juegos'),
    path('tecnologia/', tecnologia, name = 'tecnologia'),
    path('tutoriales/', tutoriales, name = 'tutoriales'),
]