from menu import display_menu
from weather import get_weather
from recipes import get_recipes
from get_random_recipe import get_random_recipe
from save_favourites import save_recipe, view_saved_recipes
from recipe_suggester import suggest_recipe_based_on_weather
from display import display_weather, display_recipes, display_random_recipe
from user_interaction import get_city_name, ask_yes_no, choose_recipe_to_save
from spotify_integration import authenticate_spotify_client, get_cooking_playlists

def main():
    print("Welcome to Weather-Recipe Buddy!")
    while True:
        try:
            choice = display_menu()
            if choice == 1:
                handle_weather_option()
            elif choice == 2:
                handle_view_favourites()
            elif choice == 3:
                handle_random_recipe()
            elif choice == 4:
                handle_generate_playlist()
            elif choice == 5:
                handle_exit()
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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

def handle_view_favourites():
    view_saved_recipes()

def handle_random_recipe():
    random_recipe = get_random_recipe()
    if random_recipe:
        display_random_recipe(random_recipe)
        if ask_yes_no("Would you like to save this recipe to your favourites?"):
            save_recipe(random_recipe, "Random")
    else:
        print("\nSorry, could not fetch a random recipe at this time.")

def handle_generate_playlist():
    sp = authenticate_spotify_client()
    if not sp:
        print("\nError: Could not connect to Spotify. Please check your credentials.")
        return

    print("\nGenerate a Cooking Playlist!")
    keyword = input("Enter a cuisine type (e.g., Italian, French) or leave blank for a random playlist: ").strip()

    # Default to "cooking" if no keyword is provided
    keyword = keyword if keyword else "cooking"

    playlists = get_cooking_playlists(sp, keyword)
    if playlists:
        print(f"\nHere are some '{keyword}' playlists you might enjoy:")
        for playlist in playlists:
            print(f"- {playlist['name']}: {playlist['description']}")
            print(f"  URL: {playlist['url']}")
    else:
        print(f"\nSorry, no playlists were found for '{keyword}'.")

def handle_exit():
    print("Thank you for using Weather-Recipe Buddy. Goodbye!")

if __name__ == "__main__":
    main()