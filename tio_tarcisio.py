valor_total = float(input("Digite o valor total da dívida: "))

juros = float(input("Juros: "))

valor_mensal_pago = float(input("Digite o valor mensal a ser pago: "))

valor_pago_com_juros = valor_mensal_pago - (valor_total * (juros / 100))
valor_2 = valor_total - valor_pago_com_juros

print("Valor restante:",valor_2)