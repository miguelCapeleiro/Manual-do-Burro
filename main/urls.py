from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    path("", views.home, name= 'home'),
    path("aluno/", views.perfil_aluno, name='perfil_aluno'),              #
]

