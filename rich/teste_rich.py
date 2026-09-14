from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

texto = Text("Olá, mundo!", justify="center")


painel = Panel(
    texto,
    width=30
)

console.print(painel)
