from django.db import models
from django.utils import timezone

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField()
    disponible_para_adopcion = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='animales_fotos/', null=True, blank=True)  # Nuevo campo para la foto

    def __str__(self):
        return self.nombre

class SolicitudAdopcion(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    mensaje = models.TextField(null=True, blank=True)
    razon_adopcion = models.TextField(
        verbose_name="¿Por qué deseas adoptar a esta mascota?",
        null=True,  # Permite valores nulos en la base de datos
        blank=True  # Permite valores vacíos en formularios
    )
    fecha_solicitud = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Solicitud de {self.nombre} para {self.animal.nombre}"