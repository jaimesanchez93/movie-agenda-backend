from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import status

class MovieListAPI(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)




class MovieDetailAPI(APIView):

    def get(self,request,id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            new_movie = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object_or_404(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
