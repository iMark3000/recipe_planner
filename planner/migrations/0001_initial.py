# Generated by Django 3.2.9 on 2021-11-04 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_website', models.CharField(default='Unknown', max_length=200)),
                ('recipe_website_name', models.CharField(default='Unknown', max_length=200)),
                ('recipe_author', models.CharField(default='Unkown', max_length=200)),
                ('recipe_description', models.TextField(default='No Description Available')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeKeywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
                ('recipe_keywords', models.ManyToManyField(to='planner.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeInstructionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction_set_name', models.CharField(max_length=200)),
                ('instruction_order', models.IntegerField()),
                ('recipe', models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.CASCADE, to='planner.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('instruction_text', models.TextField()),
                ('instruction_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.recipeinstructionset')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredientSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_component_name', models.CharField(default='Main', max_length=200)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('unit_of_measurement', models.CharField(max_length=200)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.ingredient')),
                ('ingredient_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.recipeingredientset')),
            ],
        ),
        migrations.CreateModel(
            name='PlannedMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]