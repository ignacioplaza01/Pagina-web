from django.db import models

# Create your models here.

class Equipos(models.Model):
    codEquipo = models.CharField(max_length=20)  
    marca = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    velocidadCPU = models.CharField(max_length=20)
    fechaExpiracion = models.DateField('Fecha de expiracion',blank=False, null=False)  
    def __str__(self):
        return self.codEquipo


class Trabajadores(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    equipo = models.ForeignKey(Equipos,on_delete=models.CASCADE)
    fechaAsignacion = models.CharField(max_length=20)
    
   
