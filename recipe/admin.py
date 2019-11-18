from django.contrib import admin
from .models import Ingredients, Category, Recipe, Measurements, Quantity, Steps
# Register your models here.
admin.site.register(Ingredients)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Measurements)
admin.site.register(Quantity)
admin.site.register(Steps)
