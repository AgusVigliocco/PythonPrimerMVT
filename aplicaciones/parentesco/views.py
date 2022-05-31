from django.shortcuts import redirect, render
from .models import Pariente
# Create your views here.


def home(request):
    parientesListados = Pariente.objects.all()
    return render(request, 'gestionFamiliares.html', {'parientes': parientesListados})


def registrarFamiliar(request):
    Nombre = request.POST['txtNombre']
    Apellido = request.POST['txtApellido']
    Parentesco = request.POST['txtParentesco']
    familiar = Pariente.objects.create(
        nombre=Nombre, apellido=Apellido, parentesco=Parentesco)

    return redirect('/')
