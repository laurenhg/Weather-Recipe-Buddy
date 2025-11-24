# Weather-Recipe Buddy

**Weather-Recipe Buddy** A multi-API Python application that suggests meals and cooking playlists based on real-time weather and cuisine data.
---

## Features

- **Weather-Based Recipe Suggestions**  
  Discover recipes based on the current weather and temperature in your city. Suggestions rotate between different categories for variety.
  
- **City-Specific Cuisine Mapping**  
  Get cuisine ideas based on your city name, incorporating global flavors.

- **Spotify Cooking Playlists**  
  Generate cooking playlists tailored to specific cuisines or chosen randomly.

- **Save Favorite Recipes**  
  Save your favorite recipes locally for easy access later.

- **Random Recipe Suggestions**  
  Get inspired with random recipes when you're unsure what to cook.

---

## User Menu

When you run the app, you'll be greeted with the following menu options:

1. **Get Recipes Based on Weather**  
   - Enter your city name to fetch the current weather.
   - Get recipe suggestions based on weather conditions, temperature, or city cuisine.
   - Optionally save a recipe to your favorites or explore wine pairings.

2. **View Saved Recipes**  
   - Access your saved recipes stored in a local JSON file.
   - Review recipes and use the links to view detailed instructions.

3. **Get a Random Recipe**  
   - Fetch a random recipe from the Spoonacular API.
   - Optionally save it to your favorites or generate wine pairings.

4. **Generate a Cooking Playlist**  
   - Choose a cuisine (e.g., Italian, French) or opt for a random cooking playlist.
   - Enjoy curated playlists from Spotify to enhance your cooking experience.

5. **Exit the App**  
   - Exit the application gracefully.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/laurenhg/Weather-Recipe-Buddy.git
   cd Weather-Recipe-Buddy
   
2. Set up a virtual environment:
   ```bash
    pip install -r requirements.txt
   
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Create a .env file in the root directory with the following keys:
    ```bash
   WEATHER_API_KEY=<your_weatherstack_api_key>
    SPOONACULAR_API_KEY=<your_spoonacular_api_key>
    SPOTIFY_CLIENT_ID=<your_spotify_client_id>
    SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>
***
## How to Use
1. Run the application:
   ```bash
    python3 main.py
2. Choose an option from the menu and follow the prompts:

    - Weather Recipes: Enter your city to fetch recipes based on weather conditions.
    - Saved Recipes: View your favorite recipes with links to full details.
    - Random Recipe: Get a surprise recipe suggestion.
    - Generate a Spotify playlist based on cuisine type or randomly.
    - Exit: Quit the application.

***

## APIs Used
- [WeatherStack](https://weatherstack.com) API: Fetches real-time weather data.
- [Spoonacular API](https://spoonacular.com/food-api): Provides recipes, and random recipe suggestions.  
- [Spotify API](https://developer.spotify.com/documentation/web-api): Generates personalized cooking playlists.

***

## Example User Journey
1.	Start the app and enter your city name when prompted.
2. View the weather and get recipe suggestions tailored to the weather conditions.
3.	Save a recipe to your favorites or get a wine pairing suggestion.
4.	Generate a Spotify playlist for the chosen recipe or cuisine.
5.	Access saved recipes at any time or get inspired by a random recipe.

***
 ## Acknowledgements 

Thanks to WeatherStack, Spoonacular, and Spotify for their APIs, which make this project possible.
