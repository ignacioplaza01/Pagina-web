from django import forms    
from pagina.models import Trabajadores, Equipos, Colaboradores

#Crea formularios utilizando las clases como campos

class RegistroTrabajador(forms.ModelForm):
    class Meta:
        model = Trabajadores
        fields = '__all__'

class RegistroEquipo(forms.ModelForm):

    Estados = [('activo','Activo'),('en almacen','En almacen'),('entregado','Entregado')]
    estado = forms.CharField(widget=forms.Select(choices=Estados))

    class Meta:
        model = Equipos
        fields = '__all__'        

class RegistroColab(forms.ModelForm):
    class Meta:
        model = Colaboradores
        fields = '__all__'        