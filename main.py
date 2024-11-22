from menu import display_menu
from weather import get_weather
from recipes import get_recipes
from get_random_recipe import get_random_recipe
from save_favourites import save_recipe, view_saved_recipes
from recipe_suggester import suggest_recipe_based_on_weather
from display import display_weather, display_recipes, display_random_recipe, display_wine_pairing
from user_interaction import get_city_name, ask_yes_no, choose_recipe_to_save
from wine_pairing import get_wine_pairing

def main():
    print("Welcome to Weather-Recipe Buddy!")
    while True:
        choice = display_menu()
        if choice == 1:
            handle_weather_option()
        elif choice == 2:
            handle_view_favourites()
        elif choice == 3:
            handle_random_recipe()
        elif choice == 4:
            handle_exit()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

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

            # Ask if the user wants a wine pairing suggestion
            if ask_yes_no("Would you like a wine pairing suggestion for this recipe?"):
                get_and_display_wine_pairing(selected_recipe)
        else:
            print("No recipe was saved.")
    else:
        print(f"\nSorry, no recipes found for the category '{recipe_category}'.")
        print("Please try again later or choose a different option.")

def get_and_display_wine_pairing(recipe):
    # Extract the dish name from the recipe title
    dish_name = recipe.get('title', '')
    wine_pairing = get_wine_pairing(dish_name)
    if wine_pairing:
        display_wine_pairing(wine_pairing)
    else:
        print("\nSorry, no wine pairing suggestions were found for this recipe.")

def handle_view_favourites():
    view_saved_recipes()

def handle_random_recipe():
    random_recipe = get_random_recipe()
    if random_recipe:
        display_random_recipe(random_recipe)
        if ask_yes_no("Would you like to save this recipe to your favourites?"):
            save_recipe(random_recipe, "Random")

            # Ask if the user wants a wine pairing suggestion
            if ask_yes_no("Would you like a wine pairing suggestion for this recipe?"):
                get_and_display_wine_pairing(random_recipe)
        else:
            print("No recipe was saved.")
    else:
        print("\nSorry, could not fetch a random recipe at this time.")

def handle_exit():
    print("Thank you for using Weather-Recipe Buddy. Goodbye!")

if __name__ == "__main__":
    main()