def display_menu():
    print("n\Weather-Recipe Buddy")
    print("1. Get Current Weather and Recipe Suggestions")
    print ("2. View Saves Recipes")
    print ("3. Exit")
    try:

        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0