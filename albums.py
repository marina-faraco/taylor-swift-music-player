import webbrowser

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
    if album_escolhido not in albuns:
        return []
    return list(albuns[album_escolhido].keys())

def tocar_musica(album_escolhido, musica_escolhida):
    albuns = album()
    # Verifica se album existe
    if album_escolhido not in albuns:
        return f'Esse álbum não existe 😅'

    # Verifica se a música está no album
    if musica_escolhida not in albuns[album_escolhido]:
        return f'Essa não é uma música da loirinha 😅'
    
    url = albuns[album_escolhido][musica_escolhida]
    return webbrowser.open_new(url)

