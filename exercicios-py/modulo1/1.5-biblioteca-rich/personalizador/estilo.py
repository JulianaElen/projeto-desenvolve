from rich.style import Style
from rich.console import Console
from rich.theme import Theme

console = Console()

def estilo_avisos(texto, isArquivo = False):
    """
    Gera textos no estilo de avisos, dividindo o texto em três partes e aplicando diferentes estilos de formtação.
    
    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto.
    
    Styless:
    - "info": texto em cyan sublinhado.
    - "warning": texto em magenta piscante.
    - "danger": texto em vermelho negrito.
    """
        
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    partes = len(texto) // 4
    parte1 = texto[:partes]  
    parte2 = texto[partes:2*partes]  
    parte3 = texto[2*partes:] 

    custom_theme = Theme({
    "info": "dim cyan underline",
    "warning": "magenta blink",
    "danger": "bold red"
    })

    console = Console(theme=custom_theme)
    console.print(parte1, style="info")
    console.print(parte2, style="warning")
    console.print(parte3, style="danger")

def estilo_riscado(texto, isArquivo = False):
    """
    Gera um texto riscado e com cores reversas.

    Args:
    texto (str): O texto a ser exibido ou o caminho do arquivo a ser lido.
    isArquivo (bool): Se verdadeiro, lê o conteúdo de um arquivo em vez de usar o texto direto. Defaults to False.

    Styles:
    - "strike reverse": texto riscado com cores invertidas.
    """

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as file:
            texto = file.read()

    console.print(texto, style="strike reverse")
