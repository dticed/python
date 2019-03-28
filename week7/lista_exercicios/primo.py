def n_primos(valor):
    contador = 0
    while valor >= 2:
        if eh_primo(valor):
            contador = contador + 1
            valor -= 1
        else:
            valor -= 1
    print(contador)

def eh_primo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator  <= x/2:
        fator = fator + 1
    if x % fator  == 0:
        return False
    else:
        return True
