# 🌤️ Weather-Recipe Buddy  
*A multi-API Python application that suggests meals and cooking playlists based on real-time weather and cuisine data.*

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/Uses-3_APIs-green" />
  <img src="https://img.shields.io/badge/CLI-Application-orange" />
</p>

---

## 📍 Overview  
Weather-Recipe Buddy is a Python application that blends **real-time weather data**, **recipe recommendations**, and **Spotify playlists** into one seamless cooking experience.

The app integrates **three different APIs** — WeatherStack, Spoonacular, and Spotify — and uses them to generate dynamic suggestions based on the user’s location, weather conditions, and cuisine preferences.

This project demonstrates:  
- API integration and authentication  
- Data parsing and transformation  
- Modular, maintainable Python architecture  
- Simple rule-based logic for mapping data to user recommendations  
- A cohesive end-to-end user experience  

---

## 🛠️ Tech Stack & Skills Demonstrated

**Languages & Libraries**
- Python 3.11  
- requests  
- python-dotenv  
- JSON parsing  

**Architecture & Practices**
- Modular project structure (services, handlers, helpers)  
- Multi-API integration  
- API authentication  
- CLI interface  
- `.env` configuration  
- Local JSON data storage  

**Data Skills**
- Transforming raw API responses  
- Mapping weather → cuisine categories  
- Basic recommendation logic  

---

## ✨ Features  

### 🌦️ Weather-Based Recipe Suggestions  
Enter your city and receive curated meal ideas based on:  
- temperature  
- weather conditions  
- seasonal/cuisine mapping  

---

### 🍽️ Cuisine-Based Recommendations  
Cities are matched to global cuisines.  
Example: *“Athens” → Greek cuisine inspiration.*

---

### 🎵 Spotify Cooking Playlists  
Generate playlists matched to:  
- cuisine type  
- meal suggestion  
- or random cooking vibes  

---

### ⭐ Additional Features  
- Save favorite recipes locally  
- Random recipe generator  
- Optional wine pairings  
- Clean, simple CLI menu  

---

## 🧩 User Menu  
1.	Get Recipes Based on Weather
	•	Enter your city to fetch weather data.
	•	Get recipe suggestions based on temperature, conditions, or cuisine.
	•	Optionally save a recipe or explore wine pairings.
2.	View Saved Recipes
	•	Access saved recipes in local JSON storage.
	•	View recipe links for detailed instructions.
3.	Get a Random Recipe
	•	Fetch a random recipe from Spoonacular.
	•	Optionally save it or explore wine pairing options.
4.	Generate a Cooking Playlist
	•	Choose a cuisine type or generate a random playlist.
	•	Enjoy curated Spotify cooking music.
5.	Exit

---

## 🔌 Installation  

### 1. Clone the repository  
git clone https://github.com/laurenhg/Weather-Recipe-Buddy.git
cd Weather-Recipe-Buddy

### 2. (Optional) Create a virtual environment  
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

### 3. Install dependencies  
pip install -r requirements.txt

### 4. Add environment variables  
Create a `.env` file in the project root:WEATHER_API_KEY=<your_weatherstack_api_key>
SPOONACULAR_API_KEY=<your_spoonacular_api_key>
SPOTIFY_CLIENT_ID=<your_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>

---

## ▶️ How to Use  

Run the application:
Then interact with the menu to:  
- fetch weather-based recipes  
- save favourites  
- explore cuisines  
- generate Spotify playlists  
- get random recipes  
- exit anytime  

---

## 🌐 APIs Used  

| API | Purpose |
|------|---------|
| **WeatherStack** | Fetches current weather data |
| **Spoonacular** | Recipes, cuisines, random recipes, wine pairing |
| **Spotify Web API** | Cooking playlists based on cuisine or mood |

---

## 🧭 Example User Journey  

1. Run the app and enter **Amsterdam**.  
2. App fetches temperature + weather conditions.  
3. Weather maps to cuisines or seasonal dishes.  
4. User receives curated recipe suggestions.  
5. User may:  
   - save a recipe  
   - generate a Spotify playlist  
   - explore wine pairing  
6. Continue exploring or exit.

---

## 📂 Project Structure  
Weather-Recipe-Buddy/
│
├── handlers/        # Core logic for recipes, weather, playlists
├── helpers/         # Utility functions
├── services/        # API requests (weather, recipes, spotify)
├── saved_recipes.json
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 Future Improvements  

- Add a Streamlit or Flask web UI  
- Store recipes in SQLite instead of JSON  
- Cache API responses  
- Enrich playlist logic using Spotify audio features  
- Add analytics (e.g., most-saved recipes)  
- Package as a pip-installable tool  

---

## 🙏 Acknowledgements  
Thanks to **WeatherStack**, **Spoonacular**, and **Spotify** for providing the APIs that make this project possible.


    
