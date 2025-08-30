from tkinter import *
from albums import *

def mostrar_musicas(album):
    musicas = listar_musicas(album)

    nova_janela = Toplevel(janela)
    nova_janela.title(album)
    nova_janela.geometry('320x400')

    frame = Frame(nova_janela)
    frame.pack(fill='both', expand=True, padx=8, pady=8)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    lb = Listbox(frame, yscrollcommand=scrollbar.set)
    for m in musicas:
        lb.insert(END, m)
    lb.pack(side=LEFT, fill='both', expand=True)
    scrollbar.config(command=lb.yview)

    def on_play(event=None):
        sel = lb.curselection()
        if not sel:
            return
        index = sel[0]
        musica = musicas[index]
        tocar_musica(album_escolhido=album, musica_escolhida=musica)

    # Double-click para tocar
    lb.bind('<Double-1>', on_play)
    # Enter para tocar
    lb.bind('<Return>', on_play)

# Criar janela
janela = Tk()
janela.title("Player")
janela.geometry("600x300") 

titulo = Label(janela, text="Taylor Swift Music Player", font=("Arial", 14))
titulo.grid(column=0, row=0, columnspan=3, pady=10)

for i in range(3):
    janela.grid_columnconfigure(i, weight=1)

# Botões com título dos albuns
ts_botao = Button(janela, text="Taylor Swift", command=lambda:mostrar_musicas('Taylor Swift'),width=25)
ts_botao.grid(column=0, row=1, padx=10, pady=5, sticky='ew')

f_botao = Button(janela, text='Fearless', command=lambda:mostrar_musicas('Fearless'),width=25)
f_botao.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

sn_botao = Button(janela, text='Speak Now', command=lambda:mostrar_musicas('Speak Now'),width=25)
sn_botao.grid(column=2, row=1, padx=10, pady=5, sticky='ew')

red_botao = Button(janela, text='Red', command=lambda:mostrar_musicas('Red'),width=25)
red_botao.grid(column=0, row=2, padx=10, pady=5, sticky='ew')

yr_botao = Button(janela, text='1989', command=lambda:mostrar_musicas('1989'),width=25)
yr_botao.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

rep_botao = Button(janela, text='Reputation', command=lambda:mostrar_musicas('Reputation'),width=25)
rep_botao.grid(column=2, row=2, padx=10, pady=5, sticky='ew')

lov_botao = Button(janela, text='Lover', command=lambda:mostrar_musicas('Lover'),width=25)
lov_botao.grid(column=0, row=3, padx=10, pady=5, sticky='ew')

folk_botao = Button(janela, text='Folklore', command=lambda:mostrar_musicas('Folklore'),width=25)
folk_botao.grid(column=1, row=3, padx=10, pady=5, sticky='ew')

eve_botao = Button(janela, text='Evermore', command=lambda:mostrar_musicas('Evermore'),width=25)
eve_botao.grid(column=2, row=3, padx=10, pady=5, sticky='ew')

mid_botao = Button(janela, text='Midnights', command=lambda:mostrar_musicas('Midnights'),width=25)
mid_botao.grid(column=0, row=4, padx=10, pady=5, sticky='ew')

ttpd_botao = Button(janela, text='The Tortured Poets Department', command=lambda:mostrar_musicas('The Tortured Poets Department'),width=25)
ttpd_botao.grid(column=1, row=4, padx=10, pady=5, sticky='ew')

tls_botao = Button(janela, text='The Life of a Showgirl', command='',width=25)
tls_botao.grid(column=2, row=4, padx=10, pady=5, sticky='ew')

# Criar widget de saída
resultado_label = Label(janela, text='', justify=LEFT, anchor='w')
resultado_label.grid(column=0, row=3, columnspan=3, pady=20)

janela.mainloop()
