# content of test_sample.py

def fatorial(n):
    fat = 1
    while(n > 1):
        fat = fat * n
        n = n - 1 
    return fat

def test_answer():
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(5) == 120