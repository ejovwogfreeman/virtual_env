from rest_framework import serializers
from musicapp.models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
