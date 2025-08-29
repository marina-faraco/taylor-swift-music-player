from tkinter import *
from albums import *

def mostrar_musicas(album):
    musicas = listar_musicas(album)
    resultado_label.config(text="\n".join(musicas) if isinstance(musicas, list) else musicas) # Verifica se o retorno foi uma lista de músicas

# Criar janela
janela = Tk()
janela.title("Player")
janela.geometry("300x200") 

titulo = Label(janela, text="Taylor Swift Music Player", font=("Arial", 14))
titulo.grid(column=0, row=0, columnspan=3, pady=10)

# Botões com título dos albuns
ts_botao = Button(janela, text="Taylor Swift", command=lambda:mostrar_musicas('Taylor Swift'))
ts_botao.grid(column=0, row=1)

f_botao = Button(janela, text='Fearless', command=lambda:mostrar_musicas('Fearless'))
f_botao.grid(column=1, row=1)

sn_botao = Button(janela, text='Speak Now', command=lambda:mostrar_musicas('Speak Now'))
sn_botao.grid(column=2, row=1)

red_botao = Button(janela, text='Red', command=lambda:mostrar_musicas('Red'))
red_botao.grid(column=0, row=2)

yr_botao = Button(janela, text='1989', command=lambda:mostrar_musicas('1989'))
yr_botao.grid(column=1, row=2)

rep_botao = Button(janela, text='Reputation', command=lambda:mostrar_musicas('Reputation'))
red_botao.grid(column=2, row=2)

lov_botao = Button(janela, text='Lover', command=lambda:mostrar_musicas('Lover'))
lov_botao.grid(column=0, row=3)

folk_botao = Button(janela, text='Folklore', command=lambda:mostrar_musicas('Folklore'))
folk_botao.grid(column=1, row=3)

eve_botao = Button(janela, text='Evermore', command=lambda:mostrar_musicas('Evermore'))
eve_botao.grid(column=2, row=3)

mid_botao = Button(janela, text='Midnights', command=lambda:mostrar_musicas('Midnights'))
mid_botao.grid(column=0, row=4)

ttpd_botao = Button(janela, text='The Tortured Poets Department', command=lambda:mostrar_musicas('The Tortured Poets Department'))
ttpd_botao.grid(column=1, row=4)

tls_botao = Button(janela, text='The Life of a Showgirl', command='')
tls_botao.grid(column=2, row=4)

# Criar widget de saída
resultado_label = Label(janela, text='', justify=LEFT, anchor='w')
resultado_label.grid(column=0, row=3, columnspan=3, pady=20)

janela.mainloop()
