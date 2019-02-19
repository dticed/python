def main():
    partida()

def computador_escolhe_jogada(n,m):
    for i in range(1, m+1):
        if ((n - (i + 1)) % (m + 1) == 0):
            n = n - 1
            print("O computador tirou " + str(i) + "peças.")
            if n > 0:
                print("Agora restam " + str(n) + "peças no tabuleiro.")
                usuario_escolhe_jogada(n,m)
            else:
                print("Fim do jogo! O computador ganhou!")
        else:
            n = n - m
            print("O computador tirou " + str(m) + "peças.")
            if n > 0:
                print("Agora restam " + str(n) + "peças no tabuleiro.")
                usuario_escolhe_jogada(n,m)
            else:
                print("Fim do jogo! O computador ganhou!")

def usuario_escolhe_jogada(n,m):
    retirada = int(input("Quantas peças você vai tirar? "))
    if retirada > m:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_escolhe_jogada(n,m)
    else:
        n = n - retirada
        if(n > 0):
            computador_escolhe_jogada(n,m)
        else:
            print("Fim do jogo. Você ganhou!")

def partida_isolada():
    print("Você escolheu uma partida isolada!")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    verifica_inicio(n,m)
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
    if n % (m + 1) == 0:
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

main()