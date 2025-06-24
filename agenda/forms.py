from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        Fields = ['nome', 'telefone', 'email', 'data_de_nascimento']
        widgets = {
            'data_de_nascimento' : forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d")
        }
