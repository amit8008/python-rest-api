from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    # print(list(movies.values()))
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)  #  pk=pk is very must to avoid error
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)
