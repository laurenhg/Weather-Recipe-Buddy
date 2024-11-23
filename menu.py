def display_menu():
    print("\nWeather-Recipe Buddy Menu")
    print("1. Get Weather-Based Recipe Suggestions")
    print("2. View Saved Recipes")
    print("3. Generate a Random Recipe")
    print("4. Generate a Cooking Playlist")
    print("5. Exit")
    try:
        return int(input("Enter your choice: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return 0