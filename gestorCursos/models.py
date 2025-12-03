from django.db import models
from django.contrib.auth.models import User

# ===============================================
# MODELO CURSO
# ===============================================
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=20, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


# ===============================================
# MODELO ALUMNO (CORREGIDO)
# ===============================================
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumnos')  # ← NUEVO
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"