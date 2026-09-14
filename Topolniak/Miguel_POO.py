import time


class spotify:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.curtida = 0

    def tocar(self):
        while self.duracao >= 0:
            print(f'{self.duracao:.2f}')
            self.duracao -= 0.01
            self.duracao = round(self.duracao, 2)
            time.sleep(1)

    def curtir(self):
        print(f'{self.titulo} curtida')
        self.curtida += 1

    def descurtir(self):
        if self.curtida == 0:
            print('Não há curtidas nessa música')
        else:
            self.curtida -= 1
            print('Música descurtida')

    def mostrar(self):
        print(f'{self.titulo} - {self.artista} | Curtidas: {self.curtida}')


class Playlist(spotify):
    def criar_playlist(self):
        praylist = []
        for i in range(1):  # Diminui para 2 para testar mais rápido, mude para 5 se quiser
            titulo = input('Nome da música: ')
            artista = input('Artista: ')
            tempo = float(input('Duração em minutos: '))
            listadeplay = spotify(titulo, artista, tempo)
            praylist.append(listadeplay)

        for dopamina in praylist:
            print(f"Música: {dopamina.titulo} - Artista: {dopamina.artista}")
            return dopamina


# Testando a criação da playlist
minha_playlist = Playlist("", "", 0)
play = minha_playlist.criar_playlist()
print(play)