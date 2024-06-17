# Solicita o primeiro operando e converte para float
operando1 = float(input("Digite o primeiro operando: "))

# Solicita o operador
operador = input("Digite o operador (+, -, /, *, **): ")

# Solicita o segundo operando e converte para float
operando2 = float(input("Digite o segundo operando: "))

# Verifica e realiza a operação
if operador == '+':
    resultado = operando1 + operando2
    print(f"Resultado: {operando1} + {operando2} = {resultado}")
elif operador == '-':
    resultado = operando1 - operando2
    print(f"Resultado: {operando1} - {operando2} = {resultado}")
elif operador == '/':
    if operando2 != 0:
        resultado = operando1 / operando2
        print(f"Resultado: {operando1} / {operando2} = {resultado}")
    else:
        print("Erro! Divisão por zero.")
elif operador == '*':
    resultado = operando1 * operando2
    print(f"Resultado: {operando1} * {operando2} = {resultado}")
elif operador == '**':
    resultado = operando1 ** operando2
    print(f"Resultado: {operando1} ** {operando2} = {resultado}")
else:
    print("Erro! Operação inválida.")
