from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, login_required

def home(request):
    return render(request, 'core/home.html')

class CustomLoginView(LoginView):
    template_name = 'login'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'logout'  # Redirige a 'home' después de cerrar sesión

@login_required
def editarPerfil(request):
    usuario = request
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request,"core/home.html")
        else:
            miFormulario = UserEditForm(instance=request.user)
    return render (request, "editarPerfil.html", {"miFormulario":miFormulario,"usuario":usuario})