from personalizador import layout, painel, progresso, estilo
import os
import argparse

arquivo = os.path.join(os.path.dirname(__file__), "texto.txt")

MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

FUNCOES = {
    "layout": ["layout_vertical", "layout_horizontal"],
    "painel": ["panel_destaque", "panel_divertido"],
    "progresso": ["progresso_simples", "progresso_multiplo"],
    "estilo": ["estilo_avisos", "estilo_riscado"]
}

parser = argparse.ArgumentParser(description="Ferramenta de formatação de texto com Rich")
parser.add_argument("texto", help="Texto ou caminho do arquivo a ser processado")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica se a entrada é um arquivo")
parser.add_argument("-m", "--modulo", choices=MODULOS.keys(), required=True, help="Escolha o módulo")
parser.add_argument("-f", "--funcao", required=True, help="Escolha a função do módulo")

args = parser.parse_args()

if args.arquivo:
    if not os.path.exists(args.texto):
        print(f"Erro: O arquivo '{args.texto}' não foi encontrado.")
        exit(1) 
    else:
        texto = args.texto
else:
    texto = args.texto 

modulo = MODULOS[args.modulo]
funcao = getattr(modulo, args.funcao)

funcao(texto, isArquivo=args.arquivo)


# -------------------------------------------------------------------------------------
#Testes

# print("\n- Layout Verical:")
# layout.layout_vertical("Exemplo de texto String.")
# layout.layout_vertical(arquivo, isArquivo=True)

# print("\n- Layout Horizontal:")
# layout.layout_horizontal("Exemplo de texto String.")
# layout.layout_horizontal(arquivo, isArquivo=True)

# print("\n- Painel de destaque:")
# painel.panel_destaque("Exemplo de texto String.")
# painel.panel_destaque(arquivo, isArquivo=True)

# print("\n- Painel de divertido:")
# painel.panel_divertido("Exemplo de texto String.")
# painel.panel_divertido(arquivo, isArquivo=True)

# print("\n- Progresso e renderização de texto simples:")
# progresso.progresso_simples("Exemplo de texto String.")
# progresso.progresso_simples(arquivo, isArquivo=True)

# print("\n- Progresso multiplo:")
# progresso.progresso_multiplo("Exemplo de texto String.")
# progresso.progresso_multiplo(arquivo, isArquivo=True)

# print("\n- Estilo de avisos: ")
# estilo.estilo_avisos("Exemplo de texto String.")
# estilo.estilo_avisos(arquivo, isArquivo=True)

# print("\n- Estilo de texto riscado: ")
# estilo.estilo_riscado("Exemplo de texto String.")
# estilo.estilo_riscado(arquivo, isArquivo=True)
  