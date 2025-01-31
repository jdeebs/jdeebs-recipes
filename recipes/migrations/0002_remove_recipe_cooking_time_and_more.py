# Generated by Django 4.2.16 on 2024-12-18 05:56

import django.core.validators
from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cooking_time',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time_minutes',
            field=models.IntegerField(default=20, help_text='Enter cooking time in minutes', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='No description available.', max_length=500),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time_minutes',
            field=models.IntegerField(default=10, help_text='Enter prep time in minutes', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='[{"name": "water", "quantity": 1, "unit": "cup"}]', help_text='Enter ingredients as a JSON string, e.g., \'[{"name": "flour", "quantity": 200, "unit": "g"}]\'', validators=[recipes.models.validate_ingredients]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='Unnamed Recipe', max_length=120),
        ),
    ]
