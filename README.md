# 🌤️ Weather-Recipe Buddy  
*A multi-API Python application that suggests meals and cooking playlists based on real-time weather and cuisine data.*

---

##  Overview  
Weather-Recipe Buddy is a Python application that blends **real-time weather data**, **recipe recommendations**, and **Spotify playlists** into one seamless cooking experience.

The app integrates **three different APIs** — WeatherStack, Spoonacular, and Spotify — and uses them to generate dynamic suggestions based on the user’s location, weather conditions, and cuisine preferences.

This project demonstrates:  
- API integration and authentication  
- Data parsing and transformation  
- Modular, maintainable Python architecture  
- Simple rule-based logic for mapping data to user recommendations  
- A cohesive end-to-end user experience  

---

##  Features  

###  Weather-Based Recipe Suggestions  
Enter your city and receive curated meal ideas based on:  
- temperature  
- conditions (e.g., clouds, rain, snow)  
- mapped seasonal/cuisine categories  

Suggestions rotate between categories for variety.

---

### Cuisine-Based Recommendations  
The app matches your city name to relevant global cuisines.  
(For example: “Athens” → Greek cuisine inspiration.)

---

###  Spotify Cooking Playlists  
Generate playlists matched to either:  
- the cuisine type  
- the meal suggestion  
- or purely random for fun  

Uses Spotify API client credentials, parsed and secured through `.env`.

---

###  Additional Features  
- **Save Favorite Recipes** (stored locally in JSON format)  
- **Random Recipe Generator** using Spoonacular  
- **Wine Pairing Options** (where supported by API)  
- **Clear CLI interaction menu**  

---

##  User Menu  
1.	Get Recipes Based on Weather
2.	View Saved Recipes
3.	Get a Random Recipe
4.	Generate a Cooking Playlist
5.	Exit

    ---

## Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/laurenhg/Weather-Recipe-Buddy.git
```
cd Weather-Recipe-Buddy

### 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate     # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add environment variables
Create a .env file in the project root:

WEATHER_API_KEY=<your_weatherstack_api_key>
SPOONACULAR_API_KEY=<your_spoonacular_api_key>
SPOTIFY_CLIENT_ID=<your_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>

## How to Use 
Run The Application 
python3 main.py

Interact with the menu to:
	•	fetch weather-based recipes
	•	save favourites
	•	explore new cuisines
	•	get random recipe ideas
	•	generate a Spotify playlist
	•	exit whenever you’re done

## APIs Used
API
Purpose
WeatherStack
Fetches current weather data for a given city
Spoonacular
Recipe search, cuisine recommendations, random recipes, wine pairings
Spotify Web API
Generates cuisine- or mood-based cooking playlists

## Example User Journey
	1.	Run the app and enter Amsterdam.
	2.	App fetches current temperature + conditions.
	3.	Weather → mapped to a cuisine or seasonal food category.
	4.	User receives curated recipe suggestions with links.
	5.	Optionally:
	•	Save a favorite recipe
	•	Generate a Spotify playlist based on cuisine
	•	Explore wine pairings
	6.	Exit or continue exploring random recipes.

## Project Structure

```
Weather-Recipe-Buddy/
│
├── handlers/        # Core logic for recipe, weather, playlist mapping
├── helpers/         # Reusable formatting and utility functions
├── services/        # API request logic (weather, recipe, spotify)
├── saved_recipes.json
├── main.py
├── requirements.txt
└── README.md
```

## Acknowledgements 
Thanks to WeatherStack, Spoonacular, and Spotify for providing the APIs that make this project possible.


