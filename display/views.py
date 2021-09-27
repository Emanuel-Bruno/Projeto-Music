from django.shortcuts import render
from .models import Playlist

# Create your views here.
def home(request):
    playlist = Playlist.objects.get(id=1)
    return render(
        request,
        'home.html',
        {
            'playlist': playlist
        }
    )