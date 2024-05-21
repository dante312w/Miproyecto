from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

lenguajes=[["python","c++","php"],]

def primeraPlantilla(request): 
    return render(request, 'primeraPlantilla.html', {"lenguajes" : lenguajes})

def plantillaAgregarElemento(request):
    return render(request, 'agregarElemento.html')

def agregarElemento(request):
    nombre = request.POST.get('nombre')
    anio = request.POST.get('anio')
    descargas = request.POST.get('descargas')
    nuevo_registro = [nombre, anio, descargas]
    lenguajes.append(nuevo_registro)
    return redirect('primera_plantilla')