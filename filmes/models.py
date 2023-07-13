from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
# CRIAR UMA TUPLA COM DUAS INFOS: NOME NO BD E O NOME QUE APARECE AO USUARIO
LISTA_CATEGORIAS = (
    ("ACAO", "Ação"),
    ("AVENTURA", "Aventura"),
    ("ROMANCE", "Romance"),
    ("TERROR", "Terror"),
    ("RPG", "RPG"),
    ("OUTROS", "Outros"),
)


# criar o filme
class VideoAnime(models.Model):
    titulo = models.CharField(max_length=100)  # CharField para uma linha de texto e max_length quantidade de caracteres
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)  # TextField para uma texto maior
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)  # CHOICES = opcoes que ele vai usar
    visualizacoes = models.IntegerField(default=0)  # define a quantidade de visualizacoes
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# criar os episodios
class Episodio(models.Model):
    filme = models.ForeignKey("VideoAnime", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

# criar os usuarios
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("VideoAnime")


