import requests

def get_recipes(food_category):
    api_key = ""
    url= f"https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": food_category,
        "api_key": api_key
    }

    try:
        response=requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes:{e}")
        return []