def get_city_name():
    return input("Please enter the name of your city: ").strip()

def ask_yes_no(question):
    while True:
        answer = input(f"\n{question} (y/n): ").strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Please enter 'y' or 'n'.")

def choose_recipe_to_save(recipes):
    while True:
        try:
            recipe_index = int(input("Enter the recipe number to save: ")) - 1
            if 0 <= recipe_index < len(recipes):
                return recipes[recipe_index]
            else:
                print("Invalid recipe number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")