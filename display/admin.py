from django.contrib import admin

from .models import (
    Musica,
    Playlist
)

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'cantor'
    ]

    search_fields = [
        'id',
        'titulo',
        'cantor'
    ]

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo'
    ]

    search_fields = [
        'id',
        'titulo'
    ]
    autocomplete_fields=['musicas']