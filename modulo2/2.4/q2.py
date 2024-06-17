# Solicita a temperatura em Fahrenheit ao usuário e converte para inteiro
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius
celsius = int((fahrenheit - 32) * (5/9))

# Imprime o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
