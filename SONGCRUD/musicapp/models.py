from datetime import datetime
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Song(models.Model):
    title = models.CharField(max_length = 40)
    date_released = models.DateField(default = datetime.today)
    likes = models.CharField(max_length = 10)
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.CharField(max_length = 1000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)