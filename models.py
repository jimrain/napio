from django.db import models


class PlaylistInfo(models.Model):
    name = models.CharField(max_length=32, default="")

    class Meta:
        verbose_name_plural = "Playlist Info"

    def __str__(self):
        return self.name



class ArtistInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    url = models.CharField(max_length=200)
    playlist = models.ManyToManyField(PlaylistInfo, related_name='artists')

    class Meta:
        verbose_name_plural = "Artist Info"

    def __str__(self):
        return self.name


class AlbumInfo(models.Model):
    name = models.CharField(max_length=32, default="")
    url = models.CharField(max_length=200)
    playlist = models.ManyToManyField(PlaylistInfo, related_name='albums')

    class Meta:
        verbose_name_plural = "Album Info"

    def __str__(self):
        return self.name

