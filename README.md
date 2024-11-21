# <u>**Weather Recipe Buddy**</u>

Weather-Recipe Buddy is a Python application that suggests personalized recipe ideas based on the current weather in your city. By fetching real-time weather data and leveraging a recipe API, it provides recommendations that suit the weather conditions, temperature, and even your location. You can also save your favorite recipes, organized by categories, for easy access later.
# Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
   1. [Clone the Repository](#clone)
   2. [Create a Virtual Environment (Recommended)](#create)
   3. [Install Dependencies](#install)
   4. [Set Up API Keys](#API)
4. [Usage](#usage)
5. [Running the Application](#running)
6. [Menu Options](#menu)
7. [Example Session](#example)
8. [Troubleshooting](#troubleshooting)
9. [Contact](#contact)

### Features
- **Weather-Based Recipe Suggestions**: Get recipe recommendations that match the current weather in your city.
- **Save Favorites**: Save your favorite recipes under specific categories for easy retrieval.
- **Recipe Details**: Access recipe titles and source URLs for detailed instructions.
- **User-Friendly Interface**: Simple command-line interface suitable for beginners.
- **Varied Cuisine Options**: Includes a diverse range of recipes, considering temperature, weather conditions, and location., and location.

### Prerequisites
- **Python**: Version 3.7 or higher.
- **Internet Connection**: Required to fetch data from APIs.
- **APIs**:
	- **Weatherstack API**: For fetching weather data.
	- **Spoonacular API**: For fetching recipe data.

### Installation

### 1. Clone the Repository

Clone the repository from GitHub and navigate into the project directory:

git clone https://github.com/laurenhg/weather-recipe-buddy.git
cd weather-recipe-buddy

### 2. Create a Virtual Environment (Recommended)

Creating a virtual environment helps manage dependencies:
`python -m venv venv`

Activate the virtual environment:
	- **On Windows**:`venv\Scripts\activate`
	- **On macOS/Linux**: `source venv/bin/activate`

### 3. Install Dependencies
Install the required Python packages using pip:
`pip install -r requirements.txt`

- **Note**: If requirements.txt is not provided, install the following packages: `pip install requests python-dotenv`

### 4. Set Up API Keys
The application requires API keys for:
	- **Weatherstack API** (for weather data)
	- **Spoonacular API** (for recipe data)

**Obtain API Keys**
- **Weeatherstack API Key:** Sign up for a free account at Weatherstack to get your API key.
- **Spoonaculare API Key:** Sign up for a free account at Spoonacular to get your API key.

**Creat a .env File** 
Create a file named .env in the root directory of the project and add your API keys:

dotenv
`WEATHER_API_KEY=your_weatherstack_api_key_here`
`SPOONACULAR_API_KEY=your_spoonacular_api_key_here`

**Important**: Replace your weatherstack api key and spoonacular api key with your actual API keys. Do not share your API keys publicly. 

### Usage 

**Running the Application**
Run the application using the following command:
`python main.py`

### Menu Options 
When you run the applicaiton, you will see the following menu: 
Weather-Recipe Buddy
1. Get Current Weather and Recipe Suggestions
2. View Saved Recipes
3. Exit
Enter your choice:

- **Option 1:** Get weather and recipe suggestions.
- **Option 2:** View your saved favorite recipes.
- **Option 3:** Exit the application.

### Example Session 
Welcome to Weather-Recipe Buddy!

Weather-Recipe Buddy
1. Get Current Weather and Recipe Suggestions
2. View Saved Recipes
3. Exit
Enter your choice: 1

Please enter the name of your city: Amsterdam

Current weather in Amsterdam:
Temperature: 8°C
Description: Light Rain

Based on the weather, we suggest recipes in the category: Soup.

Here are some recipes you might enjoy:
1. Creamy Tomato Soup
2. Chicken Noodle Soup
3. Vegetable Minestrone
4. Lentil Soup with Ham
5. Mushroom Barley Soup
6. French Onion Soup
7. Butternut Squash Soup
8. Potato Leek Soup
9. Clam Chowder
10. Beef Stew

Would you like to save a recipe to your favourites? (y/n): y
Enter the recipe number to save: 2

Recipe 'Chicken Noodle Soup' saved successfully under 'soup' category!

Weather-Recipe Buddy
1. Get Current Weather and Recipe Suggestions
2. View Saved Recipes
3. Exit
Enter your choice: 2

Your Saved Recipes:

Category: Soup
  1. Chicken Noodle Soup
     Link: https://www.example.com/chicken-noodle-soup

End of list.

Weather-Recipe Buddy
1. Get Current Weather and Recipe Suggestions
2. View Saved Recipes
3. Exit
Enter your choice: 3

Thank you for using Weather-Recipe Buddy. Goodbye!

### Troubleshooting
**API Key Errors**
	•	Ensure your API keys are correctly entered in the .env file.
	•	Check that there are no extra spaces or quotes around the keys.
	•	Verify that your API keys are active and have not exceeded usage limits.

**Connection Errors**:
	•	Confirm that you have a stable internet connection.
	•	Check if the APIs are accessible from your network.

**Module Not Found Errors**:
	•	Ensure all dependencies are installed:
`pip install -r requirements.txt`
	•	Activate your virtual environment if you’re using one.

**Unexpected Behaviour**
	•	Rerun the application and check for consistent issues.
	•	Look for error messages in the terminal to identify specific problems.

### Contact 

Lauren Gilbert 
Project Link: https://github.com/laurenhg/weather-recipe-buddy
