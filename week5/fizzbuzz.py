def main():
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))
    print(fizzbuzz(4))
    print(fizzbuzz(10))

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return "Fizz"
    if numero % 3 != 0 and numero % 5 == 0:
        return "Buzz"
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 != 0 and numero % 5 != 0:
        return numero

main()