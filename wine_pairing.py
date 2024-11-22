import requests
from config import SPOONACULAR_API_KEY

def get_wine_pairing(dish_name):
    if not SPOONACULAR_API_KEY:
        print("Error: SPOONACULAR_API_KEY is not set in the environment variables.")
        return None

    url = "https://api.spoonacular.com/food/wine/pairing"
    params = {
        "food": dish_name,
        "apiKey": SPOONACULAR_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get('pairedWines'):
            return {
                "pairedWines": data['pairedWines'],
                "pairingText": data['pairingText']
            }
        else:
            return {
                "pairedWines": [],
                "pairingText": "Sorry, no wine pairings available for this dish"
            }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wine pairing: {e}")
        return {
            "pairedWines": [],
            "pairingText": "An error occurred fetching wine pairings"
        }
