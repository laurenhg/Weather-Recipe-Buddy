from menu import display_menu
from handlers.weather_handler import handle_weather_option
from handlers.favourites_handler import handle_view_favourites
from handlers.random_recipe_handler import handle_random_recipe
from handlers.playlist_handler import handle_generate_playlist
from handlers.exit_handler import handle_exit

def main():
    print("Welcome to Weather-Recipe Buddy!")
    while True:
        try:
            choice = display_menu()
            if choice == 1:
                handle_weather_option()
            elif choice == 2:
                handle_view_favourites()
            elif choice == 3:
                handle_random_recipe()
            elif choice == 4:
                handle_generate_playlist()
            elif choice == 5:
                handle_exit()
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()