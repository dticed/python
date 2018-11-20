def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return "Fizz"
    if numero % 3 != 0 and numero % 5 == 0:
        return "Buzz"
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 != 0 and numero % 5 != 0:
        return numero

def test():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(4) == 4