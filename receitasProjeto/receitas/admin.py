from django.contrib import admin
from .models import Recipe


# Register your models here.

class listRecipe(admin.ModelAdmin):
    list_display = ('id', 'recipe_name', 'category', 'preparation_time')
    list_display_links = ('id', 'recipe_name')
    search_fields = ('recipe_name',)
    list_filter = ('category', )
    list_per_page = 2


admin.site.register(Recipe, listRecipe)
