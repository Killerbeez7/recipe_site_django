from django.urls import path

from recipe_site_django.recipe_app.views import list_recipes, recipe_details, like_recipe, add_recipe, edit_recipe, \
    delete_recipe, comment_recipe

urlpatterns = [
    path('', list_recipes, name='list-recipes'),
    path('details/<int:pk>', recipe_details, name='recipe-details'),
    path('like/<int:pk>', like_recipe, name='like-recipe'),
    path('add/', add_recipe, name='add-recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit-recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete-recipe'),
    path('comment/<int:pk>', comment_recipe, name='comment-recipe'),


]
