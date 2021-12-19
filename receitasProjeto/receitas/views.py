from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe


def index(request):
    recipe_data = Recipe.objects.all()

    return render(request, 'index.html', context={'recipes': recipe_data})


def receita(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    shown_recipe = {
        'recipe': recipe
    }

    return render(request, 'receita.html', shown_recipe)
