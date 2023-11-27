from django.db import models

# Create your models here.
class Usuario (models.Model):
    nome = models.CharField(max_length=50)
    data_nasc = models.DateField()
    matricula = models.CharField(max_length=10)
    data_matricula = models.DateField()
    administrador = models.BooleanField()
    
    def __str__(self):
        return self.nome
    
class Esporte (models.Model):
    nome = models.CharField(max_length=50)
    individual = models.BooleanField()
    usuarios = models.ManyToManyField()
    
    def __str__(self):
        return self.nome

class Categoria (models.Model):
    descricao = models.CharField(max_field=50)
    
    def __str__(self):
        return self.descricao
    
class Curso (models.Model):
    nome = models.CharField(max_field=100)
    categoria = models.OneToOneField('Categoria', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Torneio (models.Model):
    nome = models.CharField(max_length=50)
    ano_limite = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Equipe (models.Model):
    nome = models.CharField(max_field=50)
    torneios = models.ManyToManyField(Torneio)    
    esporte = models.OneToOneField('Esporte', on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.nome