from django import forms
from .models import Personaje, Coaching


class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['nombre', 'biography', 'introduction', 'imagen_titulo', 'imagen_personaje', 'imagen_fondo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'imagen_titulo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_personaje': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_fondo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



class CoachForm(forms.ModelForm):
    class Meta:
        model = Coaching
        fields = ['nombre', 'precio', 'descripcion', 'personaje', 'rank', 'city']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'personaje': forms.Select(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }