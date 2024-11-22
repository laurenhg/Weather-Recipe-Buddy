import requests
from dotenv import load_dotenv
import os

# Load environment variables once
load_dotenv()

def get_weather(city):

    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY is not set in the environment variables.")
        return None

    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if the API call was successful
        if 'success' in data and data['success'] == False:
            error_code = data.get('error', {}).get('code', 'Unknown')
            if error_code == 615:
                print("\nThe city name seems invalid or not found. Please check the spelling and try again.")
            else:
                print(f"\nError: {data.get('error', {}).get('info', 'An unknown error occurred.')}")
            return None

        if "current" in data and "location" in data:
            weather = {
                "temperature": data["current"]["temperature"],
                "description": data["current"]["weather_descriptions"][0],
                "city": data["location"]["name"]
            }
            return weather
        else:
            print("\nSorry, we couldn't retrieve weather data for that location.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching weather data: {e}")
        return None