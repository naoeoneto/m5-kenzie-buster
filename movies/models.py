from django.db import models
from users.models import User


# Create your models here.
class RatingMovies(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=RatingMovies.choices, default=RatingMovies.G
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="added_by", null=True
    )
    orders = models.ManyToManyField(
        User, through="movies.MovieOrder", related_name="users"
    )

    def __repr__(self) -> str:
        return f"<Movie - id: {self.id}, title: {self.title}>"


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __repr__(self) -> str:
        return f"<Movie Order - id: {self.id}, price: {self.title}, buyed at: {self.buyed_at}>"
