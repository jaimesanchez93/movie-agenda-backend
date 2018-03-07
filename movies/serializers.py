from django.contrib.auth.models import User
from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    category = serializers.CharField()
    image = serializers.ImageField()
    image_url = serializers.URLField()
    movie_seen = serializers.BooleanField()
    duration = serializers.IntegerField()

    def create(self,validated_data):
        instance = Movie()
        return self.update(instance,validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name')
        instance.category = validated_data.get('category')
        instance.image_url = validated_data.get('image_url')
        instance.movie_seen = validated_data.get('movie_seen')
        instance.duration = validated_data.get('duration')
        instance.save()
        return instance
