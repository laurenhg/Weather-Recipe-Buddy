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

        if "current" in data and "location" in data:
            weather = {
                "temperature": data["current"]["temperature"],
                "description": data["current"]["weather_descriptions"][0],
                "city": data["location"]["name"]
            }
            return weather
        else:
            print(f"Error: Unexpected API response: {data}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None