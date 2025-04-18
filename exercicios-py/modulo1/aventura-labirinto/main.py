# O arquivo principal do jogo que controla a lógica do jogo, o menu, as opções e a interação do usuário.

# Você deve implementar uma CLI para executar o main. Defina pelo menos 5 elementos (argumentos, opções, parâmetros) sendo pelo menos uma delas obrigatória. Sugestões:

# --name <nome>: Nome do(a) jogador(a)

# --color <cor>: Escolher a cor principal do jogo

# --dificuldade <x>: Crie mais de um labirinto e deixe o(a) jogador(a) escolher

# --disable-sound: Que tal colocar música no jogo com uma opção para desligar? (playsound)

# --help: Personalize o help padrão

# Aqui é onde tudo acontece. Ao iniciar, o jogo deve apresentar um menu de opções (pelo menos "instruções" e "jogar"). Nessa etapa você pode pedir o nome do(a) jogador(a) para formatar as mensagens na tela.

# Ao iniciar o jogo e imprimir o labirinto e o(a) jogador(a) na tela, se inicia um laço (infinito ou com máximo de movimentos) chamando as funções de jogo (mover, pontuar, etc.).

# Ao final, crie uma tela formatada de vitória ou derrota (talvez no módulo utils?) se despedindo do(a) jogador(a).

# Sugestão: que tal incluir aqui a sua função recursiva? Crie no módulo utils uma função recursiva que faz uma animação simples para celebrar a vitória do(a) jogador(a).

# Use a biblioteca argparse para criar a linha de comando com as opções para o jogo, como:

# --name <nome>: Nome do jogador.

# --color <cor>: Cor principal do jogo.

# --dificuldade <x>: Escolha do labirinto (fácil, médio, difícil).

# --disable-sound: Desabilitar efeitos sonoros no jogo.

# --help: Exibir informações de ajuda.

# Menu de Opções: Quando o jogo for iniciado, mostre um menu com pelo menos as opções:

# Instruções

# Jogar

# Lógica do Jogo: Imprima o labirinto e inicie um loop infinito onde o jogador pode mover-se e coletar itens, pontuar, etc. Quando o jogador terminar o jogo (vencer ou perder), exiba uma tela de vitória ou derrota.

# 4.2. Função Recursiva
# Função Recursiva de Solução: No menu, adicione uma opção para o jogador assistir a uma solução do labirinto sendo resolvida automaticamente por uma função recursiva.

# 4.3. Funções de Término
# Ao vencer o jogo, mostre uma tela de vitória.

# Ao perder o jogo, mostre uma tela de derrota. As mensagens podem ser formatadas com a biblioteca rich.