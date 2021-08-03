from django.contrib import admin

from napio.models import ArtistInfo, AlbumInfo, PlaylistInfo

admin.site.register(ArtistInfo)
admin.site.register(AlbumInfo)
admin.site.register(PlaylistInfo)
