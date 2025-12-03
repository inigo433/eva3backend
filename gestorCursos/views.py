from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Alumno, Curso
from .forms import AlumnoForm, CursoForm

# ===============================================
# VISTAS PÚBLICAS
# ===============================================

def index(request):
    """Página principal"""
    context = {
        'school_name': 'Escuela Chucky TI',
        'services': ['Desarrollo Backend', 'Gestión de Proyectos', 'Comunicación Técnica'],
    }
    return render(request, 'gestorCurso/index.html', context)


def prueba_view(request):
    """Página de prueba"""
    return render(request, 'gestorCurso/prueba.html', {})


# ===============================================
# MIXINS PERSONALIZADOS
# ===============================================

class AdminSoloMixin(UserPassesTestMixin):
    """Solo Admin (superuser o staff) puede acceder"""
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('alumno_list')


class CreadorOAdminMixin(UserPassesTestMixin):
    """Solo el creador o Admin puede acceder"""
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return self.get_object().creador == self.request.user
    
    def handle_no_permission(self):
        return redirect('alumno_list')


# ===============================================
# VISTAS CRUD ALUMNOS
# ===============================================

class AlumnoListView(LoginRequiredMixin, ListView):
    """Listar alumnos (solo del usuario o todos si es admin)"""
    model = Alumno
    template_name = 'gestorCurso/alumno_list.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            # Admin ve todos los alumnos
            return Alumno.objects.all().order_by('apellidos')
        else:
            # Usuario normal solo ve los suyos
            return Alumno.objects.filter(creador=user).order_by('apellidos')


class AlumnoCreateView(LoginRequiredMixin, CreateView):
    """Crear nuevo alumno"""
    model = Alumno
    form_class = AlumnoForm
    template_name = 'gestorCurso/alumno_form.html'
    success_url = reverse_lazy('alumno_list')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Crear Nuevo Alumno'
        return context


class AlumnoUpdateView(LoginRequiredMixin, CreadorOAdminMixin, UpdateView):
    """Editar alumno (solo creador o admin)"""
    model = Alumno
    form_class = AlumnoForm
    template_name = 'gestorCurso/alumno_form.html'
    success_url = reverse_lazy('alumno_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Editar Alumno'
        return context


class AlumnoDeleteView(AdminSoloMixin, DeleteView):
    """Eliminar alumno (solo admin)"""
    model = Alumno
    template_name = 'gestorCurso/alumno_confirm_delete.html'
    success_url = reverse_lazy('alumno_list')


# ===============================================
# VISTAS CRUD CURSOS
# ===============================================

class CursoListView(LoginRequiredMixin, ListView):
    """Listar todos los cursos"""
    model = Curso
    template_name = 'gestorCurso/curso_list.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        return Curso.objects.all().order_by('nombre')


class CursoCreateView(AdminSoloMixin, CreateView):
    """Crear curso (solo admin)"""
    model = Curso
    form_class = CursoForm
    template_name = 'gestorCurso/curso_form.html'
    success_url = reverse_lazy('curso_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Crear Nuevo Curso'
        return context


class CursoUpdateView(AdminSoloMixin, UpdateView):
    """Editar curso (solo admin)"""
    model = Curso
    form_class = CursoForm
    template_name = 'gestorCurso/curso_form.html'
    success_url = reverse_lazy('curso_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Editar Curso'
        return context


class CursoDeleteView(AdminSoloMixin, DeleteView):
    """Eliminar curso (solo admin)"""
    model = Curso
    template_name = 'gestorCurso/curso_confirm_delete.html'
    success_url = reverse_lazy('curso_list')