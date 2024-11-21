import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()

def get_recipes(food_category):
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        print("Error: SPOONACULAR_API_KEY is not set in the environment variables.")
        return []

    if not food_category:
        print("Error: Food category cannot be empty.")
        return []

    url = "https://api.spoonacular.com/recipes/complexSearch"


    max_offset = 100
    offset = random.randint(0, max_offset)

    params = {
        "query": food_category,
        "number": 10,
        "offset": offset,
        "apiKey": api_key,
        "addRecipeInformation": True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "results" in data and data["results"]:

            results = data["results"]
            for recipe in results:
                recipe.setdefault("sourceUrl", "No URL available")
            return results


        print(f"No recipes found for {food_category}. Trying a broader category...")
        fallback_category = "dinner"
        params["query"] = fallback_category
        params["offset"] = random.randint(0, max_offset)
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "results" in data:
            results = data["results"]
            for recipe in results:
                recipe.setdefault("sourceUrl", "No URL available")
            return results
        else:
            print(f"No recipes found even for fallback category: {fallback_category}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return []