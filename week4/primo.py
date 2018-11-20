numero = True

while numero:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
        print("nao primo")
        if numero == 0:
            numero = False
    else:
        print("primo")