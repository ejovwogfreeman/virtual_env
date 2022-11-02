from rest_framework.response import Response
from rest_framework.decorators import api_view
from musicapp.models import *
from .serializers import *

@api_view(['GET'])
def getAllArtists(request):
    artists = Artiste.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllSongs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSong(request, pk):
    song = Song.objects.get(id=pk)
    serializer = SongSerializer(song)
    return Response(serializer.data)

@api_view(['POST'])
def addSong(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateSong(request, pk):
    song = Song.objects.get(id=pk)
    serializer = SongSerializer(instance=song, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSong(request, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    return Response("deleted successfully.")

