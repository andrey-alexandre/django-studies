from django.shortcuts import render


def index(request):
    recipe_data = {
        1: 'Lasanha',
        2: 'Sorvete',
        3: 'Bolo',
        4: 'Bolo de pote'
    }
    return render(request, 'index.html', context={'recipe_dict': recipe_data})


def receita(request):
    return render(request, 'receita.html')
