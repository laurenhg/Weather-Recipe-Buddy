from get_random_recipe import get_random_recipe
from display import display_random_recipe
from save_favourites import save_recipe
from user_interaction import ask_yes_no

def handle_random_recipe():
    random_recipe = get_random_recipe()
    if random_recipe:
        display_random_recipe(random_recipe)
        if ask_yes_no("Would you like to save this recipe to your favourites?"):
            save_recipe(random_recipe, "Random")
    else:
        print("\nSorry, could not fetch a random recipe at this time.")