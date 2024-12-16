from django import forms
from .models import SolicitudAdopcion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['nombre', 'email', 'telefono', 'direccion', 'razon_adopcion']  # Incluye 'razon_adopcion'
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
            'razon_adopcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Explica por qué deseas adoptar esta mascota'}),
        }
