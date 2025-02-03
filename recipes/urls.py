from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, delete_recipe, add_recipe

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', RecipeListView.as_view(), name='list'),
    path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipes/delete/<int:pk>', delete_recipe, name='delete_recipe'),
    path('recipes/add/', add_recipe, name='add_recipe')
]