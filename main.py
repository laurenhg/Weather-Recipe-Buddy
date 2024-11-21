from menu import display_menu
from weather import get_weather
from recipes import get_recipes
from save_favourites import save_recipe, view_saved_recipes
from weather_to_food import suggest_recipe_based_on_weather

def main():
    print("Welcome to Weather-Recipe Buddy!")
    while True:
        choice = display_menu()
        if choice == 1:
            city = input("Please enter the name of your city: ").strip()
            weather_data = get_weather(city)
            if weather_data:
                print(f"\nCurrent weather in {weather_data['city']}:")
                print(f"Temperature: {weather_data['temperature']}°C")
                print(f"Description: {weather_data['description']}")

                recipe_category = suggest_recipe_based_on_weather(weather_data)
                print(f"\nBased on the weather, we suggest recipes in the category: {recipe_category.capitalize()}.")

                recipes = get_recipes(recipe_category)
                if recipes:
                    print("\nHere are some recipes you might enjoy:")
                    for i, recipe in enumerate(recipes, 1):
                        print(f"{i}. {recipe['title']}")
                    while True:
                        save = input("\nWould you like to save a recipe to your favourites? (y/n): ").strip().lower()
                        if save == "y":
                            try:
                                recipe_index = int(input("Enter the recipe number to save: ")) - 1
                                if 0 <= recipe_index < len(recipes):
                                    save_recipe(recipes[recipe_index], recipe_category)
                                    break
                                else:
                                    print("Invalid recipe number. Please try again.")
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        elif save == "n":
                            break
                        else:
                            print("Please enter 'y' or 'n'.")
                else:
                    print(f"\nSorry, no recipes found for the category '{recipe_category}'.")
                    print("Please try again later or choose a different option.")
            else:
                print("\nCould not fetch weather data. Please check the city name and try again.")
        elif choice == 2:
            view_saved_recipes()
        elif choice == 3:
            print("Thank you for using Weather-Recipe Buddy. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()