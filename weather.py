import requests

def get_weather(city):
    api_key = ""
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