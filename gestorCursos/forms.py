from django import forms
from .models import Alumno, Curso

class AlumnoForm(forms.ModelForm):
    """Formulario para crear/editar alumnos"""
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'fecha_nacimiento', 'curso']  # ← AHORA INCLUYE 'curso'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CursoForm(forms.ModelForm):
    """Formulario para crear/editar cursos"""
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'codigo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }