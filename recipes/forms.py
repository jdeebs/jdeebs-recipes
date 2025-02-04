from django import forms
from .models import Recipe
import json

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
        # Ingredient is separate due to JSON format requirement
        fields = ['name', 'description', 'prep_time_minutes', 'cooking_time_minutes', 'difficulty', 'pic']

    def clean(self):
        cleaned_data = super().clean()

        # Get ingredient data from the form 'POST'
        names = [name.strip() for name in self.data.getlist('ingredient_names') if name.strip()]
        quantities = [qty.strip() for qty in self.data.getlist('ingredient_quantities') if qty.strip()]
        units = [unit.strip() for unit in self.data.getlist('ingredient_units') if unit.strip()]

        # Ensure that at least one ingredient exists
        if not names or not quantities or not units:
            raise forms.ValidationError("Recipe must have at least 1 ingredient with a name, quantity, and unit.")

        # Ensure all lists have the same number of items
        if len(names) != len(quantities) or len(quantities) != len(units):
            raise forms.ValidationError("Each ingredient must have a name, quantity, and unit of measure.")

        # Convert data into JSON format
        ingredients = [{"name": names[i], "quantity": quantities[i], "unit": units[i]} for i in range(len(names))]

        # Store as JSON string
        cleaned_data['ingredients'] = json.dumps(ingredients)

        return cleaned_data