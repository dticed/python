valor = input("Digite um valor a ser somado:")

tamanho = len(valor)
divisor = 10
soma = 0

while tamanho > 0:
    resto = int(valor) % divisor
    quociente = int(valor) // divisor
    valor = quociente
    soma = soma + resto
    tamanho = tamanho - 1

print(soma)

