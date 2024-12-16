from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_animales, name='lista_animales'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('adoptar/<int:animal_id>/', views.adoptar_animal, name='adoptar_animal'),  # Detalles de adopción
]
