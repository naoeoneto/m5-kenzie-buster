from rest_framework import serializers
from movies.models import RatingMovies, Movie, MovieOrder
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(default=None)
    rating = serializers.ChoiceField(
        choices=RatingMovies.choices, default=RatingMovies.G
    )
    duration = serializers.CharField(max_length=10, default=None)
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.CharField(source="user.email", read_only=True)
    # title = serializers.SerializerMethodField()
    # buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)

    # def get_title(self, obj: Movie) -> str:
    #     return obj.title

    # def get_buyed_by(self, obj: User) -> str:
    #     return obj.email
        