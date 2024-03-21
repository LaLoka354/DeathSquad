from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
=======
>>>>>>> master
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })

<<<<<<< HEAD
def ejemplo(request):
    return HttpResponse('<p>ejemplo</p>')
=======
def novedades(request):
    posts = Post.objects.order_by('-created')[:5]
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
            Fecha_evento = request.POST.get('Fecha_evento')
        )

    return render(request, 'create_post.html')
>>>>>>> master
