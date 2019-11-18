from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Ingredients, Recipe, Quantity, Steps


class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = [
            'name',
        ]

    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Ingredients.objects.filter(name__iexact=name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError(
                "This name has already been used. Please try again.")
        return name


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ()

    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Recipe.objects.filter(name__iexact=name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError(
                "This Recipe name has already been used. Please try again.")
        return name


class QuantityForm(ModelForm):
    class Meta:
        model = Quantity
        exclude = ()


class StepsForm(ModelForm):
    class Meta:
        model = Steps
        exclude = ()


IngredientFormSet = inlineformset_factory(
    Recipe, Quantity, form=QuantityForm, extra=1)
InstructionFormSet = inlineformset_factory(
    Recipe, Steps, form=StepsForm, extra=1)
