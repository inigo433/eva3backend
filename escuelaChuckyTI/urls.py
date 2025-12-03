from django.contrib import admin
from django.urls import path, include
from gestorCursos import views as curso_views

urlpatterns = [
    # ===============================================
    # ADMIN DE DJANGO
    # ===============================================
    path('admin/', admin.site.urls),
    
    # ===============================================
    # AUTENTICACIÓN (gestorUser)
    # ===============================================
    path('accounts/', include('gestorUser.urls')),
    
    # ===============================================
    # PRINCIPAL Y GESTORCURSOS
    # ===============================================
    path('', curso_views.index, name='index'),
    path('', include('gestorCursos.urls')),
]