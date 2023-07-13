from .models import VideoAnime

def lista_filmes_recentes(request):
    lista_filmes = VideoAnime.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque" : filme_destaque}

def lista_filmes_emalta(request):
    lista_filmes = VideoAnime.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}
