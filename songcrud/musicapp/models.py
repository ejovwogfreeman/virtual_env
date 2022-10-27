from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content