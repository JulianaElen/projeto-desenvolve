import time
from rich.progress import track
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def progresso_simples(texto, isArquivo = False):
    """ 
    Exibe uma barra de progresso simples. 
     
    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.
    """

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    for i in track(range(20), description="Processando..."):
        time.sleep(1)
    
    console.print(Panel(texto))

def progresso_multiplo(texto, isArquivo=False):
    """ 
    Gera progressos multiplos.
    
    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.
    """

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    with Progress(transient=True) as progress:
        task1 = progress.add_task("[yellow]Baixando texto...", total=100)
        task2 = progress.add_task("[blue]Processando escrita...", total=100)

        while not progress.finished:
            progress.update(task1, advance=0.4)
            progress.update(task2, advance=0.6)
            time.sleep(0.02)
    
    for line in texto.splitlines():  # Dividindo o texto em linhas
        print(line)
        time.sleep(0.7) 
