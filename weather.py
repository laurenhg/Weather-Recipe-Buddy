import requests

def get_weather(city):
    api_key = "182ba813dcb21cfb58a884cb7ef2259f"
    url = f"http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "current" in data:
        weather = {
            "temperature": data["current"]["temperature"],
            "description": data["current"]["weather_descriptions"][0],
            "city": data["location"]["name"]
        }
        return weather
    else: print ("Error: unable to retrieve weather data.")
    return none
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
