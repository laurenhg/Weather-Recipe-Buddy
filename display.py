def display_weather(weather_data):
    print(f"\nCurrent weather in {weather_data['city']}:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Description: {weather_data['description']}")

def display_recipes(recipes):
    print("\nHere are some recipes you might enjoy:")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe['title']}")

def display_random_recipe(recipe):
    print("\nHere is a random recipe for you:")
    print(f"Title: {recipe['title']}")
    print(f"Link: {recipe.get('sourceUrl', 'No URL available')}")

#

def display_favourites(favourites):
    print("\nYour Saved Recipes:")
    for category, recipes in favourites.items():
        print(f"\nCategory: {category.capitalize()}")
        for i, recipe in enumerate(recipes, start=1):
            print(f"  {i}. {recipe['title']}")
            if recipe.get('sourceUrl'):
                print(f"     Link: {recipe['sourceUrl']}")
            else:
                print("     Link: Sorry, no URL currently available")
    print("\nEnd of list.")