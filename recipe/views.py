
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Ingredients, Recipe, Quantity, Steps
from .forms import AddIngredientForm, IngredientFormSet, InstructionFormSet, RecipeForm
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )


class IngredientsListView(ListView):
    model = Ingredients
    context_object_name = 'object'
    ordering = ['name']


class IngredientsDetailView(DetailView):
    model = Ingredients


class IngredientsCreateView(LoginRequiredMixin, CreateView):
    model = Ingredients
    form_class = AddIngredientForm
    success_url = '/recipe/ingredients/'


class IngredientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredients
    fields = ['name', ]


class IngredientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredients
    success_url = '/recipe/ingredients'


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'object'
    ordering = ['name']


class RecipeDetailView(DetailView):
    model = Recipe
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Quantity'] = Quantity.objects.filter(
            recipe_id=self.kwargs.get('pk'))
        context['Steps'] = Steps.objects.filter(
            recipe_id=self.kwargs.get('pk'))
        return context


class RecipeCreateView(CreateView):

    model = Recipe
    form_class = RecipeForm
    success_url = '/recipe/'

    def get(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet()
        instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
                instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()

        instruction_form.instance = self.object
        print(instruction_form.instance)
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))


class RecipeUpdateView(UpdateView):

    model = Recipe
    form_class = RecipeForm
    success_url = '/recipe/'

    def get_context_data(self, **kwargs):
        form = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            form['ingredient_form'] = IngredientFormSet(
                self.request.POST, instance=self.object)
            form['instruction_form'] = InstructionFormSet(
                self.request.POST, instance=self.object)
        else:
            form['ingredient_form'] = IngredientFormSet(instance=self.object)
            form['instruction_form'] = InstructionFormSet(instance=self.object)
        return form

    def form_valid(self, form):
        print("am I valid tho")
        context = self.get_context_data()
        ingredient_form = context['ingredient_form']
        instruction_form = context['instruction_form']
        with transaction.atomic():
            self.object = form.save()

            if ingredient_form.is_valid():
                ingredient_form.instance = self.object
                ingredient_form.save()

            if instruction_form.is_valid():
                instruction_form.instance = self.object
                instruction_form.save()

        return super(RecipeUpdateView, self).form_valid(form)

    def form_invalid(self, form, ingredient_form, instruction_form):

        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipe/'
