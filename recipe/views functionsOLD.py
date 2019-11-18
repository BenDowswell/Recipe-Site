from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredients, Recipe
from django.http import HttpResponse
from .forms import addingredient, addrecipe

# Create your views here.


def show_ingredients_view(request, *args, **kwargs):
    obj = Ingredients.objects.all()
    context = {
        'object': obj
    }
    return render(request, "recipe/show_ingredients.html", context)


def add_recipe_view(request):
    form = addrecipe(request.POST or None)
    if request.method == 'POST':
        form = addrecipe(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = addrecipe()
    context = {"form": form}
    template_name = 'recipe/add_recipe.html'
    return render(request, template_name, context)


def add_ingredients_view(request):
    form = addingredient(request.POST or None)
    if request.method == 'POST':
        form = addingredient(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = addingredient()
    context = {"form": form}
    return render(request, "recipe/add_ingredients.html", context)


def ingredient_detail_view(request, name):
    obj = get_object_or_404(Ingredients, name=name)
    template_name = "recipe/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def ingredient_update_view(request, name):
    obj = get_object_or_404(Ingredients, name=name)
    form = addingredient(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/recipe")
    template_name = 'recipe/add_ingredients.html'
    context = {"form": form}
    return render(request, template_name, context)


def ingredient_delete_view(request, name):
    obj = get_object_or_404(Ingredients, name=name)
    template_name = 'recipe/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/recipe")
    context = {"object": obj}
    return render(request, template_name, context)
