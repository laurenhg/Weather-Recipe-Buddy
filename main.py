from menu import display_menu
from weather import get_weather
from recipes import get_recipes
from weather_to_food import suggest_recipe_based_on_weather

def main():
    while True:
        choice = display_menu()
        if choice == 1:
            city = input("Enter your city: ")
            weather_data = get_weather(city)
            if weather_data:
                print(f"\nWeather in {city}:")
                print(f"Temperature: {weather_data['temperature']}°C")
                print(f"Description: {weather_data['description']}")

                recipe_category = suggest_recipe_based_on_weather(weather_data)
                print(f"\Suggested recipes for{recipe_category}:")
                recipes = get_recipes(recipe_category)

                if recipes:
                    for i, recipe in enumerate(recipes, 1):
                        print(f"{i}. {recipe[title]}")
                        save = input("Would you like to save a recipe? (y/n): ").lower()
                        if save == "y":
                            recipe_index = int(input("Enter the recipe number to save: ")) -1
                            save_recipe(recipes[recipe_index])

                        else:
                            print("No reicpes found for this category.")
                            else:
                            print("Could not fetch weather data.")
                        elif choice == 2:
                        view_saved_recipes ()
                    elif == 3:
                        print ("Goodbye!")
                        break
                else:
                    print("Invalid choice. Try again.")

                    if__name__ == "__main__":
                    main()