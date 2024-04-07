from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, default='Sin título')
    Descripcion = models.TextField(null=True)
    lugar = models.TextField(null=True, default="camino bajo la petisa")
    organiza = models.TextField(null=True)
    Fecha_evento = models.DateTimeField(null=True)
    Fecha_publicacion = models.DateTimeField(null=True)
    especificaciones = models.TextField(null=True)
    recomendaciones = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# comentario prueba 