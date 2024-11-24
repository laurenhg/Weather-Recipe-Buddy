from services.spotify_integration import authenticate_spotify_client, get_cooking_playlists

def handle_generate_playlist():
    sp = authenticate_spotify_client()
    if not sp:
        print("\nError: Could not connect to Spotify. Please check your credentials.")
        return

    print("\nGenerate a Cooking Playlist!")
    keyword = input("Enter a cuisine type (e.g., Italian, French) or leave blank for a random playlist: ").strip()

    # Default to "cooking" if no keyword is provided
    keyword = keyword if keyword else "cooking"

    playlists = get_cooking_playlists(sp, keyword)
    if playlists:
        print(f"\nHere are some '{keyword}' playlists you might enjoy:")
        for playlist in playlists:
            print(f"- {playlist['name']}: {playlist['description']}")
            print(f"  URL: {playlist['url']}")
    else:
        print(f"\nSorry, no playlists were found for '{keyword}'.")