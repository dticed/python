#programa para somar numeros adjacentes

condicao = True

while condicao:
    numero = input("Digite um número inteiro: ")
    tamanho = len(numero)
    resto = int(numero) % divisor
    quociente = int(numero) // divisor
    numero = quociente
