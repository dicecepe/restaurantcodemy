from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

def index(request):
    context = {
        'ingredients': Ingredient.objects.all(),
        'menu_items': MenuItem.objects.all(),
        'recipe_requirements': RecipeRequirement.objects.all(),
        'purchases': Purchase.objects.all(),
    }
    return render(request, 'djangodelights/index.html', context)
