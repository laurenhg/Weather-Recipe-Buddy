# Weather-Recipe- Buddy

**Weather-Recipe Buddy** is a Python-based application that combines weather data with recipe suggestions to enhance your culinary experience. This app also integrates with Spotify to generate cooking playlists for an enjoyable time in the kitchen.

---

## Features

- **Weather-Based Recipe Suggestions**  
  Get recipe ideas based on the current weather conditions and temperature in your city.

- **City-Specific Cuisine**  
  The app uses your city name to suggest recipes aligned with the local or culturally relevant cuisine.

- **Cooking Playlists with Spotify**  
  Enhance your cooking experience with curated playlists based on cuisine or a random theme.

- **Save Recipes to Favorites**  
  Store your favorite recipes in a local JSON file for easy retrieval and inspiration later.

- **Random Recipe Suggestions**  
  Not sure what to cook? Get a random recipe suggestion.

---
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/laurenhg/Weather-Recipe-Buddy.git
   cd Weather-Recipe-Buddy


2.Set up a virtual environment:
```bash
	python3 -m venv .venv
	source .venv/bin/activate

3.Install the dependencies:
```bash
	pip install -r requirements.txt

4.Set up your .env file with the following keys:

WEATHER_API_KEY=<your_weather_api_key>
SPOONACULAR_API_KEY=<your_spoonacular_api_key>
SPOTIFY_CLIENT_ID=<your_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>

Usage

1.	Run the application:

python3 main.py

2.	Follow the interactive prompts to:
	•	Enter your city to get weather-based recipe suggestions.
	•	Save recipes to favorites.
	•	Generate cooking playlists with Spotify.
	•	Retrieve random recipes or view your saved recipes.

APIs Used

	•	WeatherStack API:
Provides real-time weather data based on city input.

	•	Spoonacular API:
Fetches recipes and suggests wine pairings.

	•	Spotify API:
Generates cooking playlists based on cuisine type or a random theme.

Acknowledgments

Special thanks to the providers of the WeatherStack, Spoonacular, and Spotify APIs for making this application possible.


