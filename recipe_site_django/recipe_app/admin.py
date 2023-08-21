from django.contrib import admin

from recipe_site_django.recipe_app.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'preparation_time', 'likes_count')
    list_filter = ('name',)

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Recipe, RecipeAdmin)
