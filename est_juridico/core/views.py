from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

def home(request):
    return render(request, 'core/home.html')

class CustomLoginView(LoginView):
    template_name = 'login'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'logout'  # Redirige a 'home' después de cerrar sesión