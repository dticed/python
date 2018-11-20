import math

print("Vamos usar a fórmula de bhaskara para calcular as raizes reais de uma equacao do segundo grau")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)


if delta < 0:
  print("Não tem raizes reais")
else:
  
  if delta == 0:
    print("A equacao tem 1 raiz real.")
    x = (-b + math.sqrt(delta)) / (2*a)
    print(x)
  else:
    print("A equacao tem 2 raizes reais.")
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(x1,x2)

