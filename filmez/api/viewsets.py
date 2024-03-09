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
        url = f'http://www.omdbapi.com/?t={filmes}&apikey={chave_da_api}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if the response status code is not 200
            dados = response.json()

            title = dados.get('Title', '')
            year = dados.get('Year', '')
            runtime = dados.get('Runtime', '')
            genre = dados.get('Genre', '')
            director = dados.get('Director', '')

            print(f"Movie Title: {title}")
            print(f"Year: {year}")
            print(f"Runtime: {runtime}")
            print(f"Genre: {genre}")
            print(f"Director: {director}")

        except requests.RequestException as e:
            print(f"Error fetching movie data: {e}")

        # Handle other parts of your view logic here
        recebido = {
            'title': title,
            'year': year,
            'runtime': runtime,
            'genre': genre,
            'director':director
        }
        print(recebido)
        serializer = FilmesSerializer(data = recebido)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
