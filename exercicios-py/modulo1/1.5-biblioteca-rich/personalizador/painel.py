from rich.console import Console
from rich.panel import Panel

console = Console()

def panel_destaque(texto, isArquivo = False):
    """Exibe o texto com estilo de destaque.

    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.
    """

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    console.print(Panel(
        texto,
        title="[bold yellow]Texto Importante[/bold yellow]",
        subtitle="[italic green]Esse texto está recebendo destaque nesse artigo.[/italic green]",
        border_style="yellow",
        padding=(1, 2)
    ))

def panel_divertido(texto, isArquivo = False):
    """Exibe o texto colorido e com formatações divertidas.

    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.
    """

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    partes = len(texto) // 4
    parte1 = texto[:partes]  
    parte2 = texto[partes:2*partes]  
    parte3 = texto[2*partes:3*partes]  
    parte4 = texto[3*partes:] 

    texto_formatado = (
        "[bold bright_magenta]" + parte1 + "[/bold bright_magenta] " 
        + "[italic green]" + parte2 + "[/italic green] " 
        + "[underline blue]" + parte3 + "[/underline blue] "
        + "[bold yellow]" + parte4 + "[/bold yellow]"
    )

    console.print(texto_formatado)