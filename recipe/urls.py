"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (IngredientsListView,
                    IngredientsDetailView,
                    IngredientsCreateView,
                    IngredientsUpdateView,
                    IngredientsDeleteView,
                    RecipeCreateView,
                    RecipeListView,
                    RecipeDetailView,
                    RecipeUpdateView,
                    RecipeDeleteView
                    )


urlpatterns = [

    path('', RecipeListView.as_view(), name='recipe-home'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('add-recipe/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('<int:pk>/delete/',
         RecipeDeleteView.as_view(), name='recipe-delete'),
    path('ingredients/', IngredientsListView.as_view(), name='ingredients-home'),
    path('ingredients/<int:pk>/', IngredientsDetailView.as_view(),
         name='ingredients-detail'),
    path('new-ingredients/', IngredientsCreateView.as_view(),
         name='ingredients-create'),
    path('ingredients/<int:pk>/edit/',
         IngredientsUpdateView.as_view(), name='edit-ingredient'),
    path('ingredients/<int:pk>/delete/',
         IngredientsDeleteView.as_view(), name='delete-ingredient'),

]
