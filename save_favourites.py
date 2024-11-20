import json

FAVOURITES_FILE = "favourites.json"

def save_recipe(recipe):
    try:
        with open(FAVOURITES_FILE, "a") as file:
            file.write(json.dumps(recipe) + "\n")
        print("Recipe saved!")
    except IOError as e:
        print(f"Error saving recipe: {e}")

def view_saved_recipes():
    try:
        with open(FAVOURITES_FILE, "r") as file:
            print("\nYour Saved Recipes:")
            for line in file:
                recipe = json.loads(line.strip())
                print(f"Name: {recipe['title']}, Link: {recipe.get('sourceUrl', 'No URL available')}")
    except FileNotFoundError:
        print("No saved recipes found.")
    except IOError as e:
        print(f"Error reading saved recipes: {e}")

