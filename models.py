from django.db import models


class PlaylistInfo(models.Model):
    name = models.CharField(max_length=32, default="")

    def __str__(self):
        return self.name


class ArtistInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    url = models.URLField(max_length=200)
    playlist = models.ManyToManyField(PlaylistInfo, related_name='artists')

    def __str__(self):
        return self.name


class AlbumInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    url = models.URLField(max_length=200)
    playlist = models.ManyToManyField(PlaylistInfo, related_name='albums')

    def __str__(self):
        return self.name

