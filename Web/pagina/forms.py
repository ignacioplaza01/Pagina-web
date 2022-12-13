from django import forms    
from pagina.models import Trabajadores, Equipos

class RegistroTrabajador(forms.ModelForm):
    class Meta:
        model = Trabajadores
        fields = '__all__'

class RegistroEquipo(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = '__all__'        