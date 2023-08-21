from django.db import models

from recipe_site_django.recipe_app.models import Recipe


class Comment(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


