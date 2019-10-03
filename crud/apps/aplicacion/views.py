from django.shortcuts import render, redirect
from .models import *
from .forms import MascotaForm

def home(request):
    return render(request, 'index.html')

def crearMascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MascotaForm()
    return render(request, 'aplicacion/crear_mascota.html', {'form':form})