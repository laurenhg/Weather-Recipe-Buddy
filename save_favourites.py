import json
from datetime import datetime
from display import display_favourites

FAVOURITES_FILE = "favourites.json"

TITLE_KEY = 'title'
SOURCE_URL_KEY = 'sourceUrl'
SPOONACULAR_URL_KEY = 'spoonacularSourceUrl'
IMAGE_KEY = 'image'
SUMMARY_KEY = 'summary'

def get_valid_url(recipe):
    for url_key in [SOURCE_URL_KEY, SPOONACULAR_URL_KEY]:
        url = recipe.get(url_key)
        if url and 'spoonacular.com' not in url:
            return url
    return None

def save_recipe(recipe, category):

    try:
        with open(FAVOURITES_FILE, "r") as file:
            favourites = json.load(file)
            if isinstance(favourites, list):
                favourites = {"Uncategorized": favourites}
    except (FileNotFoundError, json.JSONDecodeError):
        favourites = {}
    except IOError as e:
        print(f"\nError reading the favourites file: {e}")
        return

    if category not in favourites:
        favourites[category] = []

    valid_url = get_valid_url(recipe)

    simplified_recipe = {
        TITLE_KEY: recipe.get(TITLE_KEY, 'No Title'),
        SOURCE_URL_KEY: valid_url,
        IMAGE_KEY: recipe.get(IMAGE_KEY, ''),
        SUMMARY_KEY: recipe.get(SUMMARY_KEY, '')
    }

    normalized_title = simplified_recipe[TITLE_KEY].strip().lower()

    for recipe_list in favourites.values():
        if any(r[TITLE_KEY].strip().lower() == normalized_title for r in recipe_list):
            print(f"\nThe recipe '{simplified_recipe[TITLE_KEY]}' is already in your favourites.")
            return

    favourites[category].append(simplified_recipe)

    try:
        with open(FAVOURITES_FILE, "w") as file:
            json.dump(favourites, file, indent=4)
        print(f"\nRecipe '{simplified_recipe[TITLE_KEY]}' saved successfully under '{category}' category!")
    except IOError as e:
        print(f"\nError saving recipe: {e}")

def view_saved_recipes():
    try:
        with open(FAVOURITES_FILE, "r") as file:
            favourites = json.load(file)
    except FileNotFoundError:
        print("\nNo saved recipes found.")
        return
    except json.JSONDecodeError as e:
        print(f"\nError decoding saved recipes: {e}")
        return
    except IOError as e:
        print(f"\nError reading saved recipes: {e}")
        return
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return

    if not favourites:
        print("\nNo saved recipes found.")
        return

    display_favourites(favourites)