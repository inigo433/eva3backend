from django.urls import path
from . import views

urlpatterns = [
    # ===============================================
    # VISTAS PÚBLICAS
    # ===============================================
    path('', views.index, name='index'),
    path('prueba/', views.prueba_view, name='prueba'),
    
    # ===============================================
    # CRUD ALUMNOS
    # ===============================================
    path('alumnos/', views.AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/crear/', views.AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/editar/<int:pk>/', views.AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/eliminar/<int:pk>/', views.AlumnoDeleteView.as_view(), name='alumno_delete'),
    
    # ===============================================
    # CRUD CURSOS
    # ===============================================
    path('cursos/', views.CursoListView.as_view(), name='curso_list'),
    path('cursos/crear/', views.CursoCreateView.as_view(), name='curso_create'),
    path('cursos/editar/<int:pk>/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('cursos/eliminar/<int:pk>/', views.CursoDeleteView.as_view(), name='curso_delete'),
]