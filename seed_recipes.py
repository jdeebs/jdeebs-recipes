# Run the following commands to add recipes to the database:
# ** Make sure you're in the project src folder **
# python manage.py shell
# exec(open('seed_recipes.py').read())

import os
import django
import json

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe_project.settings")
django.setup()

from recipes.models import Recipe

recipes = [
    {
        "name": "Banana Smoothie",
        "description": "A creamy and healthy banana smoothie.",
        "prep_time_minutes": 5,
        "cooking_time_minutes": 0,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "banana", "quantity": 2, "unit": "pcs"},
            {"name": "milk", "quantity": 300, "unit": "ml"},
            {"name": "yogurt", "quantity": 100, "unit": "g"},
            {"name": "honey", "quantity": 1, "unit": "tbsp"},
            {"name": "ice cubes", "quantity": 5, "unit": "pcs"}
        ]),
    },
    {
        "name": "Beef Tacos",
        "description": "Mexican-style tacos filled with seasoned beef and fresh toppings.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "ground beef", "quantity": 300, "unit": "g"},
            {"name": "taco seasoning", "quantity": 1, "unit": "tbsp"},
            {"name": "tortillas", "quantity": 6, "unit": "pcs"},
            {"name": "lettuce", "quantity": 1, "unit": "cup"},
            {"name": "cheese", "quantity": 100, "unit": "g"}
        ]),
    },
    {
        "name": "Caesar Salad",
        "description": "Crispy romaine lettuce tossed with Caesar dressing and croutons.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 0,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "romaine lettuce", "quantity": 200, "unit": "g"},
            {"name": "Caesar dressing", "quantity": 50, "unit": "ml"},
            {"name": "croutons", "quantity": 100, "unit": "g"},
            {"name": "Parmesan cheese", "quantity": 50, "unit": "g"},
            {"name": "lemon juice", "quantity": 1, "unit": "tbsp"}
        ]),
    },
    {
        "name": "Chicken Curry",
        "description": "A flavorful curry made with tender chicken in a rich and spiced sauce.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 30,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "chicken breast", "quantity": 300, "unit": "g"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "curry powder", "quantity": 2, "unit": "tbsp"},
            {"name": "coconut milk", "quantity": 200, "unit": "ml"},
            {"name": "garlic", "quantity": 2, "unit": "cloves"}
        ]),
    },
    {
        "name": "Chocolate Chip Cookies",
        "description": "Classic chocolate chip cookies that are crispy on the outside and soft on the inside.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 15,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "butter", "quantity": 100, "unit": "g"},
            {"name": "sugar", "quantity": 100, "unit": "g"},
            {"name": "flour", "quantity": 200, "unit": "g"},
            {"name": "chocolate chips", "quantity": 100, "unit": "g"},
            {"name": "egg", "quantity": 1, "unit": "pcs"}
        ]),
    },
    {
        "name": "Classic Pancakes",
        "description": "Fluffy pancakes served with syrup and your favorite toppings.",
        "prep_time_minutes": 5,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "flour", "quantity": 200, "unit": "g"},
            {"name": "milk", "quantity": 250, "unit": "ml"},
            {"name": "egg", "quantity": 1, "unit": "pcs"},
            {"name": "baking powder", "quantity": 1, "unit": "tbsp"},
            {"name": "butter", "quantity": 50, "unit": "g"}
        ]),
    },
    {
        "name": "Greek Salad",
        "description": "A fresh and vibrant salad with classic Mediterranean flavors.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 0,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "cucumber", "quantity": 1, "unit": "pcs"},
            {"name": "tomatoes", "quantity": 2, "unit": "pcs"},
            {"name": "feta cheese", "quantity": 100, "unit": "g"},
            {"name": "olives", "quantity": 50, "unit": "g"},
            {"name": "olive oil", "quantity": 2, "unit": "tbsp"}
        ]),
    },
    {
        "name": "Lemon Garlic Shrimp",
        "description": "Succulent shrimp sautéed in a lemon garlic butter sauce.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "shrimp", "quantity": 300, "unit": "g"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"},
            {"name": "butter", "quantity": 2, "unit": "tbsp"},
            {"name": "lemon juice", "quantity": 2, "unit": "tbsp"},
            {"name": "parsley", "quantity": 1, "unit": "tbsp"}
        ]),
    },
    {
        "name": "Margherita Pizza",
        "description": "Classic pizza with fresh tomato, mozzarella, and basil.",
        "prep_time_minutes": 20,
        "cooking_time_minutes": 15,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "pizza dough", "quantity": 1, "unit": "pcs"},
            {"name": "tomato sauce", "quantity": 150, "unit": "ml"},
            {"name": "mozzarella cheese", "quantity": 200, "unit": "g"},
            {"name": "fresh basil leaves", "quantity": 10, "unit": "pcs"},
            {"name": "olive oil", "quantity": 1, "unit": "tbsp"}
        ]),
    },
]

for recipe_data in recipes:
    Recipe.objects.create(**recipe_data)
    print(f"Added: {recipe_data['name']}")
