def main():
    '''
    Essa função será a função principal para chamar todas as outras funções do programa.

    '''
    print(vogal("a"))

#Declaração de funções
def vogal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E"  or x == "I"  or x == "O"  or x == "U":
        return True
    else:
        return False

#inicio da execução do programa
main()