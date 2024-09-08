from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('editarPerfil', views.editarPerfil, name= "editarPerfil"),
]