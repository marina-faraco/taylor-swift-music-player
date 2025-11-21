import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("As variáveis de ambiente SPOTIPY_CLIENT_ID e SPOTIPY_CLIENT_SECRET não foram carregadas!")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))


def album(): 
    albuns = {
        "Taylor Swift": "5eyZZoQEFQWRHkV2xgAeBw",
        "Fearless": "4hDok0OAJd57SGIT8xuWJH",
        "Speak Now": "5AEDGbliTTfjOB8TSm1sxt",
        "Red": "6kZ42qRrzov54LcAk4onW9",
        "1989": "1o59UpKw81iHR0HPiSkJR0",
        "Reputation": "6DEjYFkNZh67HP7R9PSZvv",
        "Lover": "1NAmidJlEaVgA3MpcPFYGq",
        "Folklore": "1pzvBxYgT6OVwJLtHkrdQK",
        "Evermore": "6AORtDjduMM3bupSWzbTSG",
        "Midnights": "1fnJ7k0bllNfL1kVdNVW1A",
        "The Tortured Poets Department": "5H7ixXZfsNMGbIE5OBSpcb",
        "The Life of a Showgirl": "6mkrNYyhrReQKarMFBlhUg"     
    }
    return albuns

def listar_albuns():
    return list(album().keys())
    
def listar_musicas(album_escolhido):
    albuns = album()
    album_id = albuns[album_escolhido]

    resultado = sp.album_tracks(album_id)

    nomes = []
    mapa_ids = {}   # nome + id

    for track in resultado["items"]:
        nome = track["name"]
        id_musica = track["id"]

        nomes.append(nome)
        mapa_ids[nome] = id_musica
    
    return nomes, mapa_ids

def tocar(musica_escolhida, mapa_ids):
    if musica_escolhida not in mapa_ids:
        return f'Esse música não existe nesse álbum😅'
    
    id_musica = mapa_ids[musica_escolhida]
    url = f"https://open.spotify.com/track/{id_musica}"
    return webbrowser.open_new(url)

