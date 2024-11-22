def display_menu():
    print("\nWeather-Recipe Buddy")
    print("1. Check Weather")
    print("2. View Saved Recipes")
    print("3. Generate a Random Recipe")
    print("4. Exit")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0