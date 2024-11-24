from services.weather import get_weather
from display import display_weather
from helpers.recipe_suggester import suggest_recipe_based_on_weather
from services.recipes import get_recipes
from save_favourites import save_recipe
from display import display_recipes
from user_interaction import get_city_name, ask_yes_no, choose_recipe_to_save

def handle_weather_option():
    city = get_city_name()
    weather_data = get_weather(city)
    if weather_data:
        display_weather(weather_data)
        if ask_yes_no("Would you like recipe suggestions?"):
            offer_recipe_suggestions(weather_data)
    else:
        print("\nCould not fetch weather data. Please check the city name and try again.")

def offer_recipe_suggestions(weather_data):
    recipe_category = suggest_recipe_based_on_weather(weather_data)
    print(f"\nBased on the weather, we suggest recipes in the category: {recipe_category.capitalize()}.")
    recipes = get_recipes(recipe_category)
    if recipes:
        display_recipes(recipes)
        if ask_yes_no("Would you like to save a recipe to your favourites?"):
            selected_recipe = choose_recipe_to_save(recipes)
            save_recipe(selected_recipe, recipe_category)
    else:
        print(f"\nSorry, no recipes found for the category '{recipe_category}'.")
        print("Please try again later or choose a different option.")