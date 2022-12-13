from django.shortcuts import render, redirect
from pagina.models import Trabajadores, Equipos
from pagina.forms import RegistroEquipo, RegistroTrabajador
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
@login_required

#Trabajadores


def indexTrabajadores(request):
  busqueda = request.GET.get("buscar")
  trabajadores = Trabajadores.objects.all()

  if busqueda:
    trabajadores = Trabajadores.objects.filter(
      Q(nombres__icontains = busqueda) |
      Q(area__icontains = busqueda) 

    ).distinct()
  return render(request, 'index/index.html',{'Trabajadores':trabajadores})

def cerrarSesion(request):
  logout(request)
  return redirect('/')


#def buscador(request):
  queryset = request.GET.get("buscador")
  print(queryset)
  pos = Trabajadores.objects.filter(nombres = True)
  if queryset:
    pos = Trabajadores.objects.filter(
      Q(nombre = queryset) |
      Q(area = queryset)
    ).distinct() 
  return render(request, 'index/index.html',pos)



def registrarTrabajador(request):
  form = RegistroTrabajador()
  if request.method == 'POST':
      form = RegistroTrabajador(request.POST)
      if form.is_valid():
          form.save()
      return indexTrabajadores(request)    
  data = {'form': form}
  return render(request, 'registroTrabajador/registroT.html',data)

def eliminarTrabajador(request,id):
  trabajador = Trabajadores.objects.get(id = id)
  trabajador.delete()
  return redirect('/')  

def actualizarTrabajador(request,id):
  ropa = Trabajadores.objects.get(id = id)
  form = RegistroTrabajador(instance=ropa)
  if request.method == 'POST':
      form = RegistroTrabajador(request.POST, instance=ropa)
      if form.is_valid():
          form.save()
      return indexTrabajadores(request)    
  data = {'form':form}
  return render(request, 'registroTrabajador/registroT.html',data)

#Equipos
def indexEquipos(request):
  
  equipos = Equipos.objects.all()
  data = {'Equipos':equipos}
  return render(request,'indexEquipo/indexEquipo.html',data)

def registrarEquipos(request):
  form = RegistroEquipo()
  if request.method == 'POST':
      form = RegistroEquipo(request.POST)
      if form.is_valid():
          form.save()
      return indexEquipos(request)    
  data = {'form': form}
  return render(request, 'registroEquipo/equipos.html',data)  
  
def eliminarEquipos(request,codEquipo):
  equipo = Equipos.objects.get(codEquipo = codEquipo)
  equipo.delete()
  return redirect('/indexE') 

def actualizarEquipo(request,codEquipo):
  equipo = Equipos.objects.get(codEquipo = codEquipo)
  form = RegistroEquipo(instance=equipo)
  if request.method == 'POST':
      form = RegistroEquipo(request.POST, instance=equipo)
      if form.is_valid():
          form.save()
      return indexEquipos(request)    
  data = {'form':form}
  return render(request,'registroEquipo/equipos.html',data)
