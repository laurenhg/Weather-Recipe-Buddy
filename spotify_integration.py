from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
import random

def authenticate_spotify_client():
    try:
        client_credentials_manager = SpotifyClientCredentials(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
        )
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp
    except spotipy.SpotifyException as e:
        print("Error: Could not authenticate with Spotify. Please check your credentials.")
        return None

def get_cooking_playlists(sp, keyword="cooking"):
    try:
        # Add random keyword modifiers for variety
        random_modifiers = ["music", "vibes", "favorites", "mix"]
        keyword += f" {random.choice(random_modifiers)}"

        # Fetch a larger pool of playlists
        results = sp.search(q=keyword, type="playlist", limit=20)
        playlists = results["playlists"]["items"]

        # Randomly select 5 playlists from the pool
        random_playlists = random.sample(playlists, min(len(playlists), 3))
        suggested_playlists = []

        for playlist in random_playlists:
            playlist_info = {
                'name': playlist["name"],
                'description': playlist.get("description", "No description available"),
                'url': playlist["external_urls"]["spotify"],
            }
            suggested_playlists.append(playlist_info)

        return suggested_playlists
    except Exception as e:
        print(f"Error fetching playlists: {e}")
        return []