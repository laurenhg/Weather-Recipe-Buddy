import json

FAVOURITES_FILE = "favourites.json"

def save_recipe(recipe, category):

    try:
        try:
            with open(FAVOURITES_FILE, "r") as file:
                favourites = json.load(file)
                # Ensure favourites is a dictionary
                if isinstance(favourites, list):
                    favourites = {"Uncategorized": favourites}
        except (FileNotFoundError, json.JSONDecodeError):
            favourites = {}


        if category not in favourites:
            favourites[category] = []

        simplified_recipe = {
            "title": recipe.get('title', 'No Title'),
            "sourceUrl": recipe.get('sourceUrl', 'No URL available'),
            "image": recipe.get('image', ''),
            "summary": recipe.get('summary', '')
        }

        normalized_title = simplified_recipe['title'].strip().lower()

        for recipes in favourites.values():
            if any(r['title'].strip().lower() == normalized_title for r in recipes):
                print(f"\nThe recipe '{simplified_recipe['title']}' is already in your favourites.")
                return

        favourites[category].append(simplified_recipe)
        with open(FAVOURITES_FILE, "w") as file:
            json.dump(favourites, file, indent=4)
        print(f"\nRecipe '{simplified_recipe['title']}' saved successfully under '{category}' category!")
    except IOError as e:
        print(f"\nError saving recipe: {e}")
    except KeyError as e:
        print(f"\nError: Missing expected key in recipe data: {e}")

def view_saved_recipes():

    try:
        with open(FAVOURITES_FILE, "r") as file:
            favourites = json.load(file)
            if not favourites:
                print("\nNo saved recipes found.")
                return

            print("\nYour Saved Recipes:")
            for category, recipes in favourites.items():
                print(f"\nCategory: {category.capitalize()}")
                for i, recipe in enumerate(recipes, start=1):
                    print(f"  {i}. {recipe['title']}")
                    print(f"     Link: {recipe.get('sourceUrl', 'No URL available')}")
        print("\nEnd of list.")
    except FileNotFoundError:
        print("\nNo saved recipes found.")
    except json.JSONDecodeError as e:
        print(f"\nError decoding saved recipes: {e}")
    except IOError as e:
        print(f"\nError reading saved recipes: {e}")