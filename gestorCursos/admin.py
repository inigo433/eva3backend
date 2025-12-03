from django.contrib import admin
from .models import Curso, Alumno

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'descripcion_corta')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'codigo')
    ordering = ('nombre',)

    def descripcion_corta(self, obj):
        return obj.descripcion[:50] + "..." if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'fecha_nacimiento', 'curso', 'creador')
    list_filter = ('curso', 'creador', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellidos')
    ordering = ('-id',)
    readonly_fields = ('creador',)

    def nombre_completo(self, obj):
        return f"{obj.nombre} {obj.apellidos}"
    nombre_completo.short_description = 'Alumno'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creador = request.user
        super().save_model(request, obj, form, change)