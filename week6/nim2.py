import sys

placar_computador = 0
placar_usuario = 0



def computador_escolhe_jogada(n,m):
    global placar_computador
    for i in range(1, m+1):
        if n == n % (m+1):
            n = n - 1
            if i > 1:  
                print("O computador tirou " + str(i) + " peças.")
            else:
                print("O computador tirou uma peça.")
            if n > 0:
                if n > 1:
                    print("Agora restam " + str(n) + " peças no tabuleiro.\n")
                else:
                    print("Agora resta apenas uma peça no tabuleiro.\n")        
                
                usuario_escolhe_jogada(n,m)
            else:
                print("Fim do jogo! O computador ganhou!\n")
                placar_computador += 1
            break
        else:
            n = n - m
            if i > 1: 
                print("O computador tirou " + str(i) + " peças.")
            else:
                print("O computador tirou uma peça.")
            if n > 0:
                if n > 1:
                    print("Agora restam " + str(n) + " peças no tabuleiro.\n")
                else:
                    print("Agora resta apenas uma peça no tabuleiro.\n") 
                usuario_escolhe_jogada(n,m)
            else:
                print("Fim do jogo! O computador ganhou!\n")
                placar_computador += 1
            break


def usuario_escolhe_jogada(n,m):
    global placar_usuario
    retirada = int(input("Quantas peças você vai tirar? "))
    print()
    if retirada > m:
        print("Oops! Jogada inválida! Tente de novo.\n")
        usuario_escolhe_jogada(n,m)
    else:
        n = n - retirada
        if retirada > 1:
            print("Você tirou " + str(retirada) + " peças.")    
        else:
            print("Você tirou uma peça.")
        if(n > 0):
            if n > 1:
                print("Agora restam " + str(n) + " peças no tabuleiro.\n")
            else:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            computador_escolhe_jogada(n,m)
        else:
            print("Fim do jogo. Você ganhou!\n")
            placar_usuario += 1

def partida_isolada():
    print("Você escolheu uma partida isolada!")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    verifica_inicio(n,m)
    return

def campeonato():
    print("Você escolheu um campeonato!\n")
    rodadas = 1
    placar = 0
    while rodadas <= 3:
        print("**** Rodada", rodadas,  "****\n")
        rodadas = rodadas + 1
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print("")
        verifica_inicio(n,m)
    return placar

def verifica_inicio(n,m):
    if n % (m + 1) == 0:
        print("Você começa!\n")
        usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!\n")
        computador_escolhe_jogada(n,m)

def partida():
    tipo_partida = input("\nBem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    print("")
    if tipo_partida == "1":
        partida_isolada()
        sys.exit()
    if tipo_partida == "2":
        campeonato()
        print("**** Final do campeonato! ****\n")
        print("Placar: Você " + str(placar_usuario) + " X " + str(placar_computador) + " Computador") 
        sys.exit()
    else:
        print("Você digitou o número errado. Encerrando jogo!")

partida()