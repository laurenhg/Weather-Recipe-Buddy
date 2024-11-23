import requests
from wine_pairing import get_wine_pairing
from config import SPOONACULAR_API_KEY

import random

def get_recipes(food_category):
    if not SPOONACULAR_API_KEY:
        print("Error: SPOONACULAR_API_KEY is not set in the environment variables.")
        return []

    if not food_category:
        print("Error: Food category cannot be empty.")
        return []

    url = "https://api.spoonacular.com/recipes/complexSearch"
    max_offset = 100
    offset = random.randint(0, max_offset)

    params = {
        "number": 5,
        "offset": offset,
        "apiKey": SPOONACULAR_API_KEY,
        "addRecipeInformation": True
    }

    valid_types = ['main course', 'side dish', 'dessert', 'appetizer', 'salad', 'bread',
                   'breakfast', 'soup', 'beverage', 'sauce', 'marinade', 'fingerfood', 'snack', 'drink']
    valid_cuisines = ['African', 'American', 'British', 'Cajun', 'Caribbean', 'Chinese',
                      'Eastern European', 'European', 'French', 'German', 'Greek', 'Indian', 'Irish',
                      'Italian', 'Japanese', 'Jewish', 'Korean', 'Latin American', 'Mediterranean',
                      'Mexican', 'Middle Eastern', 'Nordic', 'Southern', 'Spanish', 'Thai', 'Vietnamese']


    if food_category.lower() in valid_types:
        params["type"] = food_category.lower()
    elif food_category.lower() in [c.lower() for c in valid_cuisines]:
        params["cuisine"] = food_category.capitalize()
    else:
        params["query"] = food_category

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "results" in data and data["results"]:
            results = data["results"]
            for recipe in results:
                # Try to get a valid source URL
                source_url = recipe.get("sourceUrl")
                spoonacular_url = recipe.get("spoonacularSourceUrl")

                # Validate the source_url
                if source_url and "spoonacular.com" not in source_url:
                    recipe["sourceUrl"] = source_url
                elif spoonacular_url and "spoonacular.com" not in spoonacular_url:
                    recipe["sourceUrl"] = spoonacular_url
                else:
                    recipe["sourceUrl"] = None  # No valid URL available

                # Alternatively, you can accept spoonacularSourceUrl if sourceUrl is not available
                if not recipe["sourceUrl"]:
                    recipe["sourceUrl"] = None  # Explicitly set to None if no valid URL

                    dish_name = recipe.get("title", "")
                    wine_pairing = get_wine_pairing(dish_name)
                    recipe["winePairing"] = wine_pairing

            return results

        # Fallback to a broader category if no results
        print(f"No recipes found for {food_category}. Trying a broader category...")
        fallback_category = "main course"
        params["query"] = ''
        params["type"] = fallback_category
        params.pop("cuisine", None)
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "results" in data and data["results"]:
            results = data["results"]
            for recipe in results:
                # Same URL validation as above
                source_url = recipe.get("sourceUrl")
                spoonacular_url = recipe.get("spoonacularSourceUrl")

                if source_url and "spoonacular.com" not in source_url:
                    recipe["sourceUrl"] = source_url
                elif spoonacular_url and "spoonacular.com" not in spoonacular_url:
                    recipe["sourceUrl"] = spoonacular_url
                else:
                    recipe["sourceUrl"] = None

                if not recipe["sourceUrl"]:
                    recipe["sourceUrl"] = None

            return results
        else:
            print(f"No recipes found even for fallback category: {fallback_category}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return []

