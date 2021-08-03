from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/artist_info/<str:name>', views.artist_info_detail),
    path('api/v1/album_info/<str:name>', views.album_info_detail),
    path('api/v1/playlist_info/<str:name>', views.playlist_info_detail),
]