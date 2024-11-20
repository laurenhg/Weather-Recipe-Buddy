import requests
from dotenv import load_dotenv
import os


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
            print("Error: Unable to retrieve weather data.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


# Add the test code here, outside the function
if __name__ == "__main__":
    city = input("Enter a city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("Failed to fetch weather information.")