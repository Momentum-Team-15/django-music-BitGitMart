from django.shortcuts import render, redirect 
from django.views.generic import ListView 
from MuzakBlooms.forms import AlbumForm 
from .models import Album 

def index(request): 
    albums = Album.objects.all() 
    return render(request, 'MuzakBlooms/index.html', {'albums': albums})

def album_detail(request, pk):
    albums = Album.objects.get(pk=pk) 
    return render(request, 'MuzakBlooms/album_detail.html', {'albums': albums})

def create_album(request): 
    if request.method == 'POST': 
        form = AlbumForm() 
        if form.is_valid(): 
            album = form.save()   
            return redirect("home") 
    else: 
        form = AlbumForm() 
    return render(request, 'MuzakBlooms/create_album.html', {'form': form})
