from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.
def home(request):
    post = Post.objects.filter(estado= True)
    return render(request, 'index.html', {'post': post})

def generales(request):
    post = Post.objects.filter(
        estado= True, 
        categoria = Categoria.objects.get(nombre = 'Generales')
        )
    return render(request, 'generales.html', {'post': post})

def programacion(request):
    return render(request, 'programacion.html')

def video_juegos(request):
    return render(request, 'video_juegos.html')

def tecnologia(request):
    return render(request, 'tecnologia.html')

def tutoriales(request):
    return render(request, 'tutoriales.html')