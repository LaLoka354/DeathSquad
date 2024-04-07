from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })

def novedades(request):
    posts = Post.objects.all()
    return render(request, 'novedades.html', { 'posts': posts })

def reglamento(request):
    posts = Post.objects.all()
    return render(request, 'reglamento.html', { 'posts': posts })

def contacto(request):
    posts = Post.objects.all()
    return render(request, 'contacto.html', { 'posts': posts })

def create_post(request):
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST.get('title'),
            Descripcion = request.POST.get('Descripcion'),
            Fecha_evento = request.POST.get('Fecha_evento'),
            lugar = request.POST.get('lugar'),
            organiza = request.POST.get('organiza'),
            especificaciones = request.POST.get('especificaciones')
        )


