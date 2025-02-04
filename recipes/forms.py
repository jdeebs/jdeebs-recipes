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
    # Ingredient fields
    ingredient_names = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Enter ingredient names, one per line"}), required=False
    )
    ingredient_quantities = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Enter ingredient quantities, one per line"}), required=False
    )
    ingredient_units = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Enter ingredient units, one per line"}), required=False
    )
    
    class Meta:
        model = Recipe
        # Ingredient is separate due to JSON format requirement
        fields = ['name', 'description', 'prep_time_minutes', 'cooking_time_minutes', 'difficulty', 'pic']

    def clean(self):
        # Convert ingredient fields to JSON format
        cleaned_data = super().clean()

        names = cleaned_data.get('ingredient_names', '').splitlines()
        quantities = cleaned_data.get('ingredient_quantities', '').splitlines()
        units = cleaned_data.get('ingredient_units', '').splitlines()

        # Ensure equal number of ingredients, quantities, and units
        if len(names) != len(quantities) or len(quantities) != len(units):
            raise forms.ValidationError("Each ingredient must have a name, quantity, and unit of measure.")
        
        # Convert data into JSON format
        ingredients = []
        for i in range(len(names)):
            ingredients.append({"name": names[i].strip(), "quantity": quantities[i].strip(), "unit": units[i].strip()})

        # Store as JSON string
        cleaned_data['ingredients'] = json.dumps(ingredients)

        return cleaned_data