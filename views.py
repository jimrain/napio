from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from napio.models import ArtistInfo, AlbumInfo, PlaylistInfo
from napio.serializers import ArtistInfoSerializer, AlbumInfoSerializer, PlaylistInfoSerializer


@csrf_exempt
def artist_info_detail(request, name):
    try:
        info = ArtistInfo.objects.get(name=name)
    except ArtistInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArtistInfoSerializer(info)
        return JsonResponse(serializer.data)


@csrf_exempt
def album_info_detail(request, name):
    try:
        info = AlbumInfo.objects.get(name=name)
    except AlbumInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AlbumInfoSerializer(info)
        return JsonResponse(serializer.data)

@csrf_exempt
def playlist_info_detail(request, name):
    try:
        info = PlaylistInfo.objects.get(name=name)
    except PlaylistInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlaylistInfoSerializer(info)
        return JsonResponse(serializer.data)
