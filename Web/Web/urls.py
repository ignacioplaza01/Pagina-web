"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pagina import views


#Aqui se definen las rutas que se utilizaran para acceder a las diferentes vistas de la pagina
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.cerrarSesion, name='salir'),
    path('', views.indexTrabajadores),
    path('registroT/', views.registrarTrabajador),
    path('eliminarT/<int:id>', views.eliminarTrabajador),
    path('actualizarT/<int:id>', views.actualizarTrabajador),
    path('indexE/', views.indexEquipos),
    path('registroE/', views.registrarEquipos),
    path('eliminarE/<str:codEquipo>', views.eliminarEquipos),
    path('actualizarE/<str:codEquipo>', views.actualizarEquipo),
    path('infoT/<int:id>', views.InfoT),
    path('infoE/<str:codEquipo>', views.InfoE)
   
]
