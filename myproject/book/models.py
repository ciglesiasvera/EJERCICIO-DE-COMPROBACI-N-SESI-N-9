from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000)
        ]
    )

class Meta:
    permissions = [
        ("development", "Permiso como Desarrollador"),
        ("scrum_master", "Permiso como Scrum Master"),
        ("product_owner", "Permiso como Product Owner"),
    ]

    def __str__(self):
        return self.title
