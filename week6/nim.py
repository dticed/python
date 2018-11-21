def main():
    partida()

def computador_escolhe_jogada(n,m):
    return

def usuario_escolhe_jogada(n,m):
    return

def partida():
    tipo_partida = input("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    
    if tipo_partida == "1":
        print("Você escolheu uma partida isolada!")
    if tipo_partida == "2":
        print("Você escolheu um campeonato!")
        rodadas = 1
        while rodadas <= 3:
            print("**** Rodada ****", rodadas)
            rodadas = rodadas + 1
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))

    
    computador_escolhe_jogada(n,m)
    usuario_escolhe_jogada(n,m)

main()