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
from .views import (show_ingredients_view,
                    add_ingredients_view,
                    ingredient_detail_view,
                    ingredient_update_view,
                    ingredient_delete_view,
                    add_recipe_view,


                    )

urlpatterns = [

    path('', show_ingredients_view),
    path('add-ingredients/', add_ingredients_view),
    path('ingredients/<str:name>/', ingredient_detail_view),
    path('ingredients/<str:name>/edit/', ingredient_update_view),
    path('ingredients/<str:name>/delete/', ingredient_delete_view),
    path('add-recipe/', add_recipe_view),
]
