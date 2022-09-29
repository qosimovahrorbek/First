from distutils.command.upload import upload
from django.db import models



class User(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    STATUS = (
        (1, 'musicant'),
        (2, 'user'),
    )
    types = models.IntegerField(choices=STATUS, default=2)    
    date_born = models.DateField()
    img = models.ImageField(upload_to='image/', null=True, blank=True)

class Music(models.Model):
    name = models.CharField(max_length=300)
    musicant = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='image/')
    music = models.FileField(upload_to='musics/')
    min = models.IntegerField()
    sec = models.IntegerField()

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
