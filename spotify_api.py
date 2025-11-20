import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="95f93c8ad16e417ebf794a0542f71eb9",
    client_secret="3da4a2fa42154c60873ff802ed9a9f78",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state,user-modify-playback-state",
    cache_path=".cache" # salva o token
))

def tocar_musica(uri):
    try:
        sp.start_playback(uris=[uri])
        return f'Tocando {uri}'
    except Exception as e:
        return f'Erro ao tentar tocar música: {e}'
    
def pausar_musica(uri):
    try:
        sp.pause_playback()
        return 'Música pausada'
    except Exception as e: 
        return f'Erro ao pausar: {e}'
    
def continuar_muisca():
    try:
        sp.start_playback()
        return 'Música retomada'
    except Exception as e:
        return f'Erro ao retomar: {e}'

def proxima_musica():
    try:
        sp.next_track()
        return 'Próxima música'
    except Exception as e:
        return f'Próxima música!'
    
def musica_atual():
    try:
        sp.current_playback()
        if musica and musica["is_playing"]:
            nome = musica["item"]["name"]
            return f'Tocando agora: {nome}'
        else:
            return "Nenhuma música tocando."
    except Exception as e:
        return f'Erro ao obter faixa atual: {e}'

print(tocar_musica('spotify:track:22kXvw7mAvMvyZxPnhYzaa'))
print(musica_atual) 