from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('login/',login , name='login'),
    path('usuarios/', usuarios, name='usuarios'),
    path('equipes', equipes, name='equipes'),
    path('cursos', cursos, name='cursos'),
    path('esportes', esportes, name='esportes'),
    path('torneios', torneios, name='torneios'),
]
