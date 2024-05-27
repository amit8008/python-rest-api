from watchlist_app.models import Shows, StreamPlatform
from watchlist_app.api.serializers import ShowsSerializers, StreamPlatformSerializers
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView


class ShowListAV(APIView) :
    def get(self, request) :
        shows = Shows.objects.all()
        serializer = ShowsSerializers(shows, many = True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = ShowsSerializers(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)


class ShowDetailAV(APIView) :
    def get(self, request, pk) :
        try :
            show = Shows.objects.get(pk = pk)
        except Shows.DoesNotExist :
            return Response({"error" :"Show not found"}, status = status.HTTP_404_NOT_FOUND)

        serializer = ShowsSerializers(show)
        return Response(serializer.data)

    def put(self, request, pk) :
        show = Shows.objects.get(pk = pk)
        serializer = ShowsSerializers(show, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

    def delete(self, request, pk) :
        show = Shows.objects.get(pk = pk)
        show.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class StreamPlatformListAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializers(platform, many = True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView) :
    def get(self, request, pk) :
        try :
            platform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist :
            return Response({"error" :"Show not found"}, status = status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializers(platform)
        return Response(serializer.data)

    def put(self, request, pk) :
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializers(platform, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

    def delete(self, request, pk) :
        platform = StreamPlatform.objects.get(pk = pk)
        platform.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializers(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
