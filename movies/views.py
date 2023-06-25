from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    """Movies list"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movies_list': movies})


class MovieDetailView(View):
    """Movie description"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})



