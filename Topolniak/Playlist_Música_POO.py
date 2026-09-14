class Musica:
    def __init__(self, titulo, artista, duracao, curtidas):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.curtidas = curtidas

    def tocar(self):
        print(f'A Música que está sendo reproduzida é {self.titulo}')

    def curtir(self):
        self.curtidas += 1

    def descurtir(self):
        if self.curtidas == 0:
            print(f'Não á curtidas na Música: {self.titulo}')
        else:
            self.curtidas -= 1

    def mostrar_dados(self):
        print('')
        print(f'Titulo: {self.titulo} | Artista: {self.artista} | Duração da Música: {self.duracao} | Quantidade de Curtidas: {self.curtidas}')

musica1 = Musica('War pigs', 'BLACK SABBATH', '7:56',  2)
musica1.tocar()
musica1.curtir()
musica1.mostrar_dados()
musica1.descurtir()
musica1.mostrar_dados()


musica2 = Musica('Paranoid', 'BLACK SABBATH', '2:48', 2)
musica3 = Musica('Iron Man', 'BLACK SABBATH', '5:53', 1)
musica4 = Musica('BLACK SABBATH', 'BLACK SABBATH', '6:20', 1)
musica5 = Musica('Senjutsu', 'Iron Maiden', '4:12', 2)
musica6 = Musica('The Number of the Beast', 'Iron Maiden', '4:50', 0)

playlist = [musica1, musica2, musica3, musica4, musica5, musica6]

for musica in playlist:
    musica.mostrar_dados()

print('')

for musica in playlist:
    if musica.curtidas >= 2:
        musica.mostrar_dados()