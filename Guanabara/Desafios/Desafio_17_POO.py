from rich.panel import Panel
from rich.console import Console
from rich.align import Align
console = Console()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto = Align.center(f'{self.nome}\n{'-'*20}\nR${self.preco:,.2f}')
        console.print(Panel(texto, width=30, title='Produto'))

c1 = Produto('iPhone 17 Pro Max', 25000.85)
c1.etiqueta()