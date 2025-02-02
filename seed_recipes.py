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
        "name": "Minestrone Soup",
        "description": "A hearty Italian vegetable soup with beans and pasta.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 30,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "carrot", "quantity": 2, "unit": "pcs"},
            {"name": "celery", "quantity": 2, "unit": "stalks"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "pasta", "quantity": 100, "unit": "g"},
            {"name": "beans", "quantity": 200, "unit": "g"}
        ]),
    },
    {
        "name": "Shrimp Scampi",
        "description": "Juicy shrimp in a garlic and butter sauce over pasta.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 15,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "shrimp", "quantity": 300, "unit": "g"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"},
            {"name": "butter", "quantity": 100, "unit": "g"},
            {"name": "white wine", "quantity": 100, "unit": "ml"},
            {"name": "pasta", "quantity": 200, "unit": "g"}
        ]),
    },
    {
        "name": "Spaghetti Bolognese",
        "description": "Classic Italian pasta dish with rich, meaty tomato sauce.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 40,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "ground beef", "quantity": 400, "unit": "g"},
            {"name": "tomato sauce", "quantity": 500, "unit": "ml"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "garlic", "quantity": 2, "unit": "cloves"},
            {"name": "spaghetti", "quantity": 300, "unit": "g"}
        ]),
    },
    {
        "name": "Vegetable Lasagna",
        "description": "Layered lasagna with a variety of fresh vegetables.",
        "prep_time_minutes": 20,
        "cooking_time_minutes": 50,
        "difficulty": "hard",
        "ingredients": json.dumps([
            {"name": "lasagna noodles", "quantity": 250, "unit": "g"},
            {"name": "ricotta cheese", "quantity": 200, "unit": "g"},
            {"name": "spinach", "quantity": 150, "unit": "g"},
            {"name": "zucchini", "quantity": 1, "unit": "pcs"},
            {"name": "tomato sauce", "quantity": 400, "unit": "ml"}
        ]),
    },
    {
        "name": "Vegetable Stir-Fry",
        "description": "Quick and healthy stir-fry with a variety of vegetables and sauce.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "bell peppers", "quantity": 2, "unit": "pcs"},
            {"name": "broccoli", "quantity": 100, "unit": "g"},
            {"name": "carrot", "quantity": 1, "unit": "pcs"},
            {"name": "soy sauce", "quantity": 2, "unit": "tbsp"},
            {"name": "garlic", "quantity": 2, "unit": "cloves"}
        ]),
    },
    {
        "name": "Vegetarian Chili",
        "description": "Hearty chili packed with beans, veggies, and spices.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 30,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "kidney beans", "quantity": 400, "unit": "g"},
            {"name": "black beans", "quantity": 400, "unit": "g"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "bell pepper", "quantity": 2, "unit": "pcs"},
            {"name": "chili powder", "quantity": 1, "unit": "tbsp"}
        ]),
    },
]

for recipe_data in recipes:
    Recipe.objects.create(**recipe_data)
    print(f"Added: {recipe_data['name']}")
