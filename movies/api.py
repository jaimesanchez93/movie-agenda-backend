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


    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            new_movie = serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def update(self,instance,validated_data):
        ''