from django import forms
from .models import Recipe

CHART__CHOICES = (
    ('#1', 'Bar chart: Ingredient Frequency'),
    ('#2', 'Pie chart: Recipes by Difficulty'),
    ('#3', 'Line chart: Recipes Total Time')
)

class RecipeChartForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'prep_time_minutes', 'cooking_time_minutes', 'difficulty', 'ingredients', 'pic']