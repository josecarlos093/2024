from django import forms
from .models import TipoSensor

class TipoSensorForm(forms.ModelForm):
    class Meta:
        model = TipoSensor
        fields = ['tipo', 'Sigla', 'descricao']  # Campos que o formulário vai exibir