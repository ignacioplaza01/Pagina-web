from django.shortcuts import render, redirect, get_object_or_404
from pagina.models import Trabajadores, Equipos, Colaboradores
from pagina.forms import RegistroEquipo, RegistroTrabajador, RegistroColab
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required

#Trabajadores
#Esto permite recuperar los datos ingresados de los trabajadores
def indexTrabajadores(request):
  
  trabajadores = Trabajadores.objects.all()

  #Permite realizas busquedas por medio de filtros(--
  busqueda = request.GET.get("buscar")
  if busqueda:
    trabajadores = Trabajadores.objects.filter(
      Q(nombres__icontains = busqueda) |
      Q(area__icontains = busqueda) |
      Q(apellidos__icontains = busqueda)
    ).distinct()#--)

  return render(request, 'index/index.html',{'Trabajadores':trabajadores})

#Permite cerrar sesion
def cerrarSesion(request):
  logout(request)
  return redirect('/')

#Permite registrar trabajadores por medio de un formulario
def registrarTrabajador(request):
  form = RegistroTrabajador()
  if request.method == 'POST':
      form = RegistroTrabajador(request.POST)
      if form.is_valid():
          form.save()
      return indexTrabajadores(request)    
  data = {'form': form}
  return render(request, 'registroTrabajador/registroT.html',data)

#Permite eliminar trabajadores de la lista
def eliminarTrabajador(request,id):
  trabajador = Trabajadores.objects.get(id = id)
  trabajador.delete()
  return redirect('/')  

#Permite actualizar los datos de los trabajores
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

def infoT(request,id):

    trabajadores = get_object_or_404(Trabajadores,pk=id)
    return render(request, 'info/infoT.html',{"Trabajadores":trabajadores})  


#Equipos
#Permite recuperar los datos de los equipos ingresados 
def indexEquipos(request):
  
  equipos = Equipos.objects.all()

  #Permite realizas busquedas por medio de filtros(--
  busqueda = request.GET.get("buscar")
  if busqueda:
    equipos = Equipos.objects.filter(
      Q(marca__icontains = busqueda) |
      Q(estado__icontains = busqueda) 

    ).distinct#--)

  return render(request,'indexEquipo/indexEquipo.html',{'Equipos':equipos})

#Permite registrar equipos por medio de un formulario
def registrarEquipos(request):
  form = RegistroEquipo()
  if request.method == 'POST':
      form = RegistroEquipo(request.POST)
      if form.is_valid():
          form.save()
      return indexEquipos(request)    
  data = {'form': form}
  return render(request, 'registroEquipo/equipos.html',data)  

#Permite eliminar equipos de la lista  
def eliminarEquipos(request,codEquipo):
  equipo = Equipos.objects.get(codEquipo = codEquipo)
  equipo.delete()
  return redirect('/indexE') 

#Permite actualizar los datos de los equipos de la lista
def actualizarEquipo(request,codEquipo):
  equipo = Equipos.objects.get(codEquipo= codEquipo)
  form = RegistroEquipo(instance=equipo)
  if request.method == 'POST':
      form = RegistroEquipo(request.POST, instance=equipo)
      if form.is_valid():
          form.save()
      return indexEquipos(request)    
  data = {'form':form}
  return render(request,'registroEquipo/equipos.html',data)

def infoE(request,codEquipo):

    equipos = get_object_or_404(Equipos,pk=codEquipo)
    return render(request, 'info/infoE.html',{"Equipos":equipos})  



def indexColab(request):
  
  colaboradores = Colaboradores.objects.all()

  busqueda = request.GET.get("buscar")
  if busqueda:
    colaboradores = Colaboradores.objects.filter(
      Q(nombres__icontains = busqueda) |
      Q(area__icontains = busqueda) |
      Q(apellidos__icontains = busqueda)
    ).distinct()#--)

  return render(request, 'colab/colab.html',{'Colaboradores':colaboradores})



def registrarColab(request):
  form = RegistroColab()
  if request.method == 'POST':
      form = RegistroColab(request.POST)
      if form.is_valid():
          form.save()
      return indexColab(request)    
  data = {'form': form}
  return render(request, 'registroC/registroC.html',data)


def eliminarColab(request,id):
  colaboradores = Colaboradores.objects.get(id = id)
  colaboradores.delete()
  return redirect('/indexC')  

def actualizarColab(request,id):
  colaboradores = Colaboradores.objects.get(id = id)
  form = RegistroColab(instance=colaboradores)
  if request.method == 'POST':
      form = RegistroColab(request.POST, instance=colaboradores)
      if form.is_valid():
          form.save()
      return indexColab(request)    
  data = {'form':form}
  return render(request, 'registroC/registroC.html',data)

def infoC(request,id):

    colaboradores = get_object_or_404(Colaboradores,pk=id)
    return render(request, 'info/infoC.html',{"Colaboradores":colaboradores})  