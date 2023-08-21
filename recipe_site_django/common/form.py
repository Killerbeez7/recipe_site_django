from django import forms

from recipe_site_django.common.models import Comment
from recipe_site_django.recipe_app.models import Recipe


class CommentForm(forms.ModelForm):
    recipe_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'recipe_pk')

    def save(self, commit=True):
        recipe_pk = self.cleaned_data['recipe_pk']
        recipe = Recipe.objects.get(pk=recipe_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            recipe=recipe,
        )

        if commit:
            comment.save()

        return comment

