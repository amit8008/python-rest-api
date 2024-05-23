from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view()
def movie_detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializer = MovieSerializers(movies)
    return Response(serializer.data)
