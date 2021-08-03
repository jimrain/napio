from rest_framework import serializers
from napio.models import AlbumInfo, ArtistInfo, PlaylistInfo

class AlbumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumInfo
        fields = ['name', 'url']

class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistInfo
        fields = ['name', 'url']

class PlaylistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistInfo
        fields = ['name', 'artists', 'albums']