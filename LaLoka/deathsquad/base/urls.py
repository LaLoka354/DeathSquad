from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
<<<<<<< HEAD
    path('ejemplo/', views.ejemplo)
=======
    path('home/', views.home),
    path('novedades/', views.novedades),
    path('reglamento/', views.reglamento),
    path('contacto/', views.contacto),
    path('create/', views.create_post)
>>>>>>> master
]