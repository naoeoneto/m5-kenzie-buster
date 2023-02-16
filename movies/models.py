from django.db import models


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

    def __repr__(self) -> str:
        return f"<Movie - id: {self.id}, title: {self.title}>"
