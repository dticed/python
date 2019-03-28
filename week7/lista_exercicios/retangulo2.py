largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

simbolo = "#"
espaco = " "
altura_fixa = altura

while altura > 0:
    if altura == 1 or altura == altura_fixa:
        print(largura * simbolo)
        altura = altura - 1
    else:
        print("#" + (largura - 2) * espaco + "#")
        altura = altura - 1