from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()  # Obtener todas las tareas de la base de datos
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})
