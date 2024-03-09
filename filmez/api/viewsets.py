from rest_framework import viewsets
from filmez.api import serializers
from filmez import models
from rest_framework.response import Response
from .serializers import FilmesSerializer
import requests


class FilmesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all()

    def create(self, request):
        filmes = request.data.get('filme', '')
        chave_da_api = "96d40779"
        url = f'http://www.omdbapi.com/?i={filmes}&apikey={chave_da_api}'
        response = requests.get.url
        dados = response.json()
        title = dados.get('title','')
        year = dados.get('year', '')
        runtime = dados.get('runtime', '')
        genre = dados.get('genre', '')
        director = dados.get('director', '')

        recebido = {
            'title': title,
            'year': year,
            'runtime': runtime,
            'genre': genre,
            'director':director
        }

        serializer = FilmesSerializer(data = recebido)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
