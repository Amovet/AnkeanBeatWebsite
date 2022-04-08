
from rest_framework import generics
from .models import PlayList
from .serializers import PlaylistSerializer
# Create your views here.



class ankeansiteAPIList(generics.ListCreateAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlaylistSerializer

