def display_menu():
    while True:
        print("\nWeather-Recipe Buddy")
        print("1. Get Current Weather and Recipe Suggestions")
        print("2. View Saved Recipes")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")