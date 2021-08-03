from django.db import models

class ArtistInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class AlbumInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class PlaylistInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    artists = models.ManyToManyField(ArtistInfo)
    albums = models.ManyToManyField(AlbumInfo)

    def __str__(self):
        return self.name
