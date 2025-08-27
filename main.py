from albums import *
import webbrowser

# Listar os albuns
print(listar_albuns())
# Escolher album
album_escolhido = input("Escolha um album: ").capitalize()
# Listar músicas
print(listar_musicas(album_escolhido))
# Escolher música
musica_escolhida = input("Escolha uma música: ")
# Tocar música
print(tocar_musica(album_escolhido, musica_escolhida))

