from rest_framework import serializers
from .models import PlayList


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ('id',
                  'title',
                  'time',
                  'cover',
                  'beat',
                  'bpm',
                  'price',
                  'tag',
                  'link')

