from django.db import models

class Musica(models.Model):

    titulo = models.CharField(
        verbose_name="Titulo",
        max_length=255,
        blank=False,
        null=True
    )
    
    cantor = models.CharField(
        verbose_name="Cantor",
        max_length=63,
        blank=True,
        null=True
    )
    
    def validate_file_extension(value):
        import os
        from django.core.exceptions import ValidationError
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = ['.mp3']

        if not ext.lower() in valid_extensions:
            raise ValidationError('Somente arquivos .mp3 são válidos')
    
    musica = models.FileField(
		verbose_name="Musica",
		help_text='Adicione aqui musicas no formato .mp3',
		upload_to='musics/',
		blank=True, null=True,
        validators=[validate_file_extension]
	)

    url = models.URLField(
        verbose_name='URL',
        null=True, blank=False
    )
    

    def __str__(self):
        
        if self.cantor:

            return ('{} - {}').format(self.cantor, self.titulo)

        return ('{}').format(self.titulo)

    class Meta:
        app_label='display'
        verbose_name='Musica'
        verbose_name_plural='Musicas'