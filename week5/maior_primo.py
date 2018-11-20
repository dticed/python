def maior_primo(x):
    while x >= 2:
        if primo(x):
            return x
        else:
            x = x - 1

def primo(x):
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    else:
        return True

print(maior_primo(7))