from django.shortcuts import render
from .models import *


# Create your views here.
def login(request):
    return render(request, "auth/login.html")


def usuarios(request):
    usuariosData = Usuario.objects.raw(
    """
    SELECT 
        u.id,
        u.nome, 
        u.data_nasc, 
        u.matricula, 
        u.data_matricula ,
        u.administrador,
        c.nome AS nome_curso ,
        ctg.descricao
    FROM app_usuario u
    INNER JOIN app_curso c
        ON u.curso_id = c.id
    INNER JOIN app_categoria ctg
        ON c.categoria_id = ctg.id
    ORDER BY u.nome                               
    """
    )

    usuarios={"usuarios": usuariosData}
        
    print(usuariosData)
        
    return render(request, "usuarios.html", usuarios)

def equipes(request):
    
    equipes_info = Equipe.objects.prefetch_related('torneios', 'esporte', 'usuarios').all()

    equipes = {'equipes':equipes_info}
    
    return render(request, "equipes.html", equipes)

def cursos(request):
    
    cursos_info = Curso.objects.prefetch_related('categoria').all()
    
    cursos = {'cursos': cursos_info}
    
    return render(request, "cursos.html", cursos)    

def esportes(request):
    
    esportes_info = Esporte.objects.prefetch_related('usuarios').all()
    
    esportes = {'esportes':esportes_info}
    
    return render(request, "esportes.html", esportes)

def torneios(request):
    
    torneios_info = Torneio.objects.all()
    
    torneios = {'torneios': torneios_info}
    
    return render(request, "torneios.html", torneios)
    
