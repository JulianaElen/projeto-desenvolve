from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()

def layout_vertical(texto, isArquivo = False):
    """
    Exibe o texto em dois layouts verticais, superior e inferior.
     
    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.
    """

    layout = Layout()

    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
        
        #Dividi o texto em duas partes:
        meio = len(texto) // 2
        primeiro_paragrafo = texto[:meio]
        segundo_paragrafo = texto[meio:]

        layout["upper"].update(Panel(primeiro_paragrafo, style="cyan"))
        layout["lower"].update(Panel(segundo_paragrafo, style="bold magenta"))
        
    else:
        layout["upper"].update(Panel(texto, style="cyan"))
        layout["lower"].update(Panel(texto, style="magenta"))
    
    console.print(layout)

def layout_horizontal(texto, isArquivo = False):
    """
    Exibe o texto em dois layouts horizontais, esquerda e direita.

    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.
    """

    layout = Layout()

    layout.split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()
        
        #Dividi o texto em duas partes:
        meio = len(texto) // 2
        primeiro_paragrafo = texto[:meio]
        segundo_paragrafo = texto[meio:]

        layout["left"].update(Panel(primeiro_paragrafo, style="red"))
        layout["right"].update(Panel(segundo_paragrafo, style="blue"))
        
    else:
        layout["left"].update(Panel(texto, style="red"))
        layout["right"].update(Panel(texto, style="blue"))
    
    console.print(layout)
