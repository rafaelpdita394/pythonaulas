# Solicita o primeiro número e converte para inteiro
numero1 = int(input("Digite o primeiro número: "))

# Solicita o segundo número e converte para inteiro
numero2 = int(input("Digite o segundo número: "))

# Calcula a soma dos dois números
soma = numero1 + numero2

# Verifica se a soma é par ou ímpar
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
