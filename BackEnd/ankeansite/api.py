from .models import PlayList
from rest_framework import viewsets, permissions
from .serializers import PlaylistSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = PlayList.objects.all()
    permissions_classes = [
       permissions.AllowAny
    ]
    serializer_class = PlaylistSerializer
