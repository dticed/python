def main():
    partida()

def computador_escolhe_jogada(n,m):
    return

def usuario_escolhe_jogada(n,m):
    retirada = int(input("Quantas peças você vai tirar? "))
    if retirada > m:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_escolhe_jogada(n,m)
    else:
        n = n - retirada
    return n

def partida_isolada():
    print("Você escolheu uma partida isolada!")
    verifica_inicio()
    return

def campeonato():
    print("Você escolheu um campeonato!")
    rodadas = 1
    while rodadas <= 3:
        print("**** Rodada", rodadas,  "****")
        rodadas = rodadas + 1
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        verifica_inicio(n,m)
    return

def verifica_inicio(n,m):
    if n % (m + 1):
        print("Você começa!")
        usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!")
        computador_escolhe_jogada(n,m)

def partida():
    tipo_partida = input("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    if tipo_partida == "1":
        partida_isolada()
    if tipo_partida == "2":
        campeonato()
    else:
        print("Você digitou o número errado. Encerrando jogo!")

        
    computador_escolhe_jogada(n,m)
    usuario_escolhe_jogada(n,m)

main()