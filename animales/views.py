from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, SolicitudAdopcion
from .forms import SolicitudAdopcionForm
from django.contrib import messages

def lista_animales(request):
    animales = Animal.objects.filter(disponible_para_adopcion=True)
    return render(request, 'animales/lista_animales.html', {'animales': animales})

def adoptar_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.animal = animal
            solicitud.save()
            # Mensaje personalizado con el nombre del animal
            messages.success(
                request,
                f'¡Tu solicitud para adoptar a {animal.nombre} ha sido enviada exitosamente! '
                'Nos pondremos en contacto contigo pronto.'
            )
            return redirect('lista_animales')
    else:
        form = SolicitudAdopcionForm()
    
    return render(request, 'animales/adoptar_animal.html', {
        'form': form,
        'animal': animal
    })

def servicios(request):
    return render(request, 'animales/servicio.html')  

def contacto(request):
    return render(request, 'animales/contacto.html')