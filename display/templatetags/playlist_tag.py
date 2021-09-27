from django import template

register = template.Library()

from display.models import Playlist

@register.simple_tag
def playlist_atual():
    
    playlist = Playlist.objects.get(id=1)
    return playlist