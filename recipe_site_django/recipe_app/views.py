from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from recipe_site_django.common.form import CommentForm
from recipe_site_django.recipe_app.forms import RecipeForm, EditRecipeForm
from recipe_site_django.recipe_app.models import Recipe, Like


def list_recipes(request):
    all_recipes = Recipe.objects.all()

    context = {
        'recipes': all_recipes,
    }

    return render(request, 'recipes/list_recipes.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.likes_count = recipe.like_set.count()
    context = {
        'recipe': recipe,
        'comment_form': CommentForm(
            initial={
                'recipe_pk': pk,
            }
        ),
        'comments': recipe.comment_set.all(),
    }

    return render(request, 'recipes/recipe_details.html', context)


def comment_recipe(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('recipe-details', pk)


def like_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    like = Like(
        recipe=recipe,
    )
    like.save()
    return redirect('recipe-details', recipe.id)


@login_required()
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-recipes')
    else:
        form = RecipeForm()

    context = {
        'form': form,
    }

    return render(request, 'recipes/add_recipe.html', context)


@login_required
def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('list-recipes')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/edit_recipe.html', context)


@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('list-recipes')
    else:
        context = {
            'recipe': recipe,
        }
        return render(request, 'recipes/delete_recipe.html', context)
