from django.db import models


class Recipe(models.Model):
    NAME_MAX = 20
    DESC_MAX = 100

    name = models.CharField(
        max_length=NAME_MAX,
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=DESC_MAX,
        null=True,
        blank=True,
    )

    preparation_time = models.PositiveIntegerField(
        models.Min(1),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to='recipe_images',
    )


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
