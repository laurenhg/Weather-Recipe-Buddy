import requests
from config import SPOONACULAR_API_KEY
import os

def get_random_recipe():
    if not SPOONACULAR_API_KEY:
        print("Error: SPOONACULAR_API_KEY is not set in the environment variables.")
        return None

    url = "https://api.spoonacular.com/recipes/random"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "number": 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "recipes" in data and data["recipes"]:
            recipe = data["recipes"][0]

            # Try to get a valid source URL
            source_url = recipe.get("sourceUrl")
            spoonacular_url = recipe.get("spoonacularSourceUrl")

            if source_url and "spoonacular.com" not in source_url:
                recipe["sourceUrl"] = source_url
            elif spoonacular_url and "spoonacular.com" not in spoonacular_url:
                recipe["sourceUrl"] = spoonacular_url
            else:
                recipe["sourceUrl"] = None  # No valid URL available

            return recipe
        else:
            print("No random recipes found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random recipe: {e}")
        return None