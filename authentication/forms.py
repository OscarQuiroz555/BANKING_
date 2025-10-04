from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'abrev', 'status']  # si tu modelo usa 'abrev', está bien
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abrev': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
