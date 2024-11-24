# Weather-Recipe Buddy

**Weather-Recipe Buddy** is a Python-based application that combines weather data with recipe suggestions to enhance your culinary experience. This app also integrates with Spotify to generate cooking playlists for an enjoyable time in the kitchen.

---

## Features

- **Weather-Based Recipe Suggestions**  
  Get recipe ideas based on the current weather conditions and temperature in your city.

- **City-Specific Cuisine**  
  The app uses your city name to suggest recipes aligned with the local or culturally relevant cuisine.

- **Wine Pairing**  
  Find the perfect wine to complement your chosen recipe using the Spoonacular API.

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

	2.	Set up a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

	3.	Install the dependencies:

pip install -r requirements.txt

	4.	Set up your .env file with the following keys:

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

Project Structure

The project is organized for modularity and maintainability:

Weather-Recipe-Buddy/
│
├── helpers/
│   ├── __init__.py        # Helper functions for various utilities.
│   ├── cuisine_mapping.py # Maps cities to relevant cuisines.
│
├── services/
│   ├── __init__.py        # Service-related utilities for external integrations.
│   ├── weather.py         # Handles WeatherStack API calls.
│
├── handlers/
│   ├── weather_handler.py # Handles weather-related logic.
│   ├── favourites_handler.py # Manages viewing favorite recipes.
│   ├── random_recipe_handler.py # Fetches random recipes.
│   ├── playlist_handler.py # Handles Spotify playlist generation.
│   ├── exit_handler.py    # Handles application exit logic.
│
├── config.py              # Configuration and constants.
├── main.py                # Entry point of the application.
├── requirements.txt       # Python dependencies.
└── .gitignore             # Ensures sensitive files like .env are ignored.

APIs Used

	•	WeatherStack API:
Provides real-time weather data based on city input.
	•	Spoonacular API:
Fetches recipes and suggests wine pairings.
	•	Spotify API:
Generates cooking playlists based on cuisine type or a random theme.

Acknowledgments

Special thanks to the providers of the WeatherStack, Spoonacular, and Spotify APIs for making this application possible.


