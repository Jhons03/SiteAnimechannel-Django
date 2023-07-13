from django.contrib import admin
from .models import VideoAnime, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(VideoAnime)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
