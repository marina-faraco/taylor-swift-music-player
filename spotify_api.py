import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="95f93c8ad16e417ebf794a0542f71eb9",
    client_secret="3da4a2fa42154c60873ff802ed9a9f78",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state,user-modify-playback-state"
))

def tocar_musica_sp(uri):
    return sp.start_playback(uris=[uri])


tocar_musica_sp("spotify:track:22kXvw7mAvMvyZxPnhYzaa")

