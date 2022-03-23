from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    post = Post.objects.filter(estado= True)
    return render(request, 'index.html', {'post': post})

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detalle_post': post})

def generales(request):
    post = Post.objects.filter(
        estado= True, 
        categoria = Categoria.objects.get(nombre__iexact = 'Generales')
        )
    return render(request, 'generales.html', {'post': post})

def programacion(request):
    return render(request, 'programacion.html')

def video_juegos(request):
    return render(request, 'video_juegos.html')

def tecnologia(request): 
    post = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnología')
    )
    return render(request, 'tecnologia.html', {'post': post})

def tutoriales(request):
    return render(request, 'tutoriales.html')
