# Generated by Django 3.2.7 on 2021-09-24 17:47

import display.models.musica
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_playlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'verbose_name': 'Playlist', 'verbose_name_plural': 'Playlist'},
        ),
        migrations.AlterField(
            model_name='musica',
            name='musica',
            field=models.FileField(help_text='Adicione aqui musicas no formato .mp3', null=True, upload_to='musics/', validators=[display.models.musica.Musica.validate_file_extension], verbose_name='Musica'),
        ),
    ]
