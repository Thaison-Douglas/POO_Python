from rich.panel import Panel
from rich import print
from rich.console import Console

console = Console()

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quant = quantidade


    def analisar(self):
        print(Panel(
            f'Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\nCada participante comerá 0.4K e cada Kg custa R$82.40\nRecomendo [blue]comprar {self.quant*0.4:.3f}Kg[/] de carne\nO custo será de [green]R${(self.quant*0.4)*82.40:,.2f}[/]\nCada pessoa pagará [yellow]R${((self.quant*0.4)*82.40)/self.quant}[/] para participar.',
            title=f'{self.titulo}', width=60))


c1 = Churrasco('Churras dos Amigos', 100)
c1.analisar()