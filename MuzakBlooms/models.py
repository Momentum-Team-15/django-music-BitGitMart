# from django.conf import settings 
from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser): 
    pass 

class Song(models.Model): 
    name = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    song_file = models.FileField(null=True, blank=True)

class Album(models.Model): 
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self): 
        return f"{self.title} by {self.artist}" 


class Artist(models.Model): 
    name = models.CharField(max_length=200)

    def __str__(self): 
        return f"{self.name}" 
