from django.db import models
from .musica import Musica

class Playlist(models.Model):

    titulo = models.CharField(
        verbose_name="Titulo",
        help_text="Adicione um titulo que descreve sua playlist",
        max_length=255,
        blank=False,
        null=True
    )

    musicas = models.ManyToManyField(
        Musica,
        verbose_name="Músicas"
    )

    def __str__(self):
        return ('{}').format(self.titulo)

    class Meta:
        app_label='display'
        verbose_name='Playlist'
        verbose_name_plural='Playlist'