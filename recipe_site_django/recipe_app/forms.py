import os
from os.path import join

from django import forms
from django.conf import settings

from recipe_site_django.core.forms import BootstrapFormMixin
from recipe_site_django.recipe_app.models import Recipe


class RecipeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            )
        }


class EditRecipeForm(RecipeForm):
    def save(self, commit=True):
        db_recipe = Recipe.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_recipe.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Recipe
        fields = '__all__'

