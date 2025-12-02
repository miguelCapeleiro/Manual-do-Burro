from django.shortcuts import render

def home(request):

    return render(request, 'site/home.html')

def perfil_aluno(request):
    return render(request, 'site/perfil_aluno.html')

def perfil_professores(request):
    return render(request, 'site/perfil_professores.html')