from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# ===============================================
# LOGIN
# ===============================================
def login_user(request):
    """Vista de inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or 'index'
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    return render(request, 'gestorCurso/login.html', {'form': form})


# ===============================================
# LOGOUT
# ===============================================
def logout_user(request):
    """Vista para cerrar sesión"""
    logout(request)
    return redirect('index')


# ===============================================
# REGISTRO (OPCIONAL)
# ===============================================
class RegisterView(CreateView):
    """Vista para registrar nuevos usuarios"""
    model = User
    form_class = UserCreationForm
    template_name = 'gestorCurso/register.html'
    success_url = reverse_lazy('login')