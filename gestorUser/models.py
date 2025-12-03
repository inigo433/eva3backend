from django.db import models
from django.contrib.auth.models import User

# Por ahora usamos el User de Django por defecto
# Si necesitas campos adicionales, puedes extenderlo aquí

class Perfil(models.Model):
    """Modelo opcional para extender User"""
    ROLES = [
        ('admin', 'Administrador'),
        ('usuario', 'Usuario Normal'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='usuario')
    
    def __str__(self):
        return f"{self.user.username} - {self.rol}"