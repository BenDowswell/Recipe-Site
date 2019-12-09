from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/recipe/ingredients/{self.pk}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/recipe/Category/{self.name}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


class Recipe(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    food_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    #picture_item = models.CharField(max_length=120)
    prep_time = models.CharField(max_length=120)
    cook_time = models.CharField(max_length=120)

    def get_absolute_url(self):
        return f"/recipe/{self.pk}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


class Measurements(models.Model):
    measurement_name = models.CharField(max_length=120)

    def __str__(self):
        return self.measurement_name

    def get_absolute_url(self):
        return f"/recipe/measurement/{self.name}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


class Quantity(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE)
    Ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurements, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Steps(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE)
    step_number = models.DecimalField(max_digits=5, decimal_places=1)
    step_description = models.CharField(max_length=120)
