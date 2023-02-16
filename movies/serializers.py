from rest_framework import serializers
from movies.models import RatingMovies
from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(default=None)
    rating = serializers.ChoiceField(
        choices=RatingMovies.choices, default=RatingMovies.G
    )
    duration = serializers.CharField(max_length=10, default=None)
    added_by = serializers.EmailField(source='user.email', read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
