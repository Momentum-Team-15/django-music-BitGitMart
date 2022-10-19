from django.conf import settings 
from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser): 
    birthday = models.DateField(blank=True, null=True) 

class Album(models.Model): 
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    # ForeignKey represents a O2M relationship. The 'One' is 
    # the field and the 'Many' are from the class it is defined 
    # on (many=mre than one)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self): 
        return f"{self.title} by {self.artist}" 


class Artist(models.Model): 
    name = models.CharField 

    def __str__(self): 
        return f"{self.name}"

