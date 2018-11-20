def vogal(x):
    '''
    função para verificar se é ou nao vogal.
    '''
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E"  or x == "I"  or x == "O"  or x == "U":
        return True
    else:
        return False

def test_answer():
    assert vogal("a") == True
    assert vogal("b") == False
    assert vogal("c") == False
    assert vogal("e") == True
    assert vogal("i") == True
    assert vogal("o") == True
    assert vogal("u") == True
    assert vogal("A") == True
    assert vogal("E") == True
    assert vogal("I") == True
    assert vogal("O") == True
    assert vogal("U") == True
    assert vogal("z") == False
    assert vogal("x") == False
    assert vogal("y") == False