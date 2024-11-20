import requests
from dotenv import load_dotenv
import os


load_dotenv()

def get_recipes(food_category):
    # Fetch the API key from the .env file
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        print("Error: SPOONACULAR_API_KEY is not set in the environment variables.")
        return []


    if not food_category:
        print("Error: Food category cannot be empty.")
        return []


    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": food_category,
        "number": 5,  # Fetch 5 recipes
        "apiKey": api_key
    }

    try:

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()


        if "results" in data:
            return data["results"]
        else:
            print("Error: Unexpected response structure.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return []