from rest_framework import viewsets
from filmez.api import serializers
from filmez import models

class FilmesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all()