from pickletools import read_decimalnl_short

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
from dotenv import load_dotenv

def authenticate_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def get_cooking_playlists(sp, keyword="cooking"):
    results = sp.search(q=keyword, type="playlist", limit=10)
    playlists = results["playlists"]["items"]
    suggested_playlists = []

    for playlist in playlists:
        playlist_info = {
            'name': playlist["name"],
            'description': playlist.get("description", "No description available"),
            'url': playlist["external_urls"]["spotify"],
        }
        suggested_playlists.append(playlist_info)
        return suggested_playlists