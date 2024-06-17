# Solicita a idade de Juliana e converte para inteiro
idade_juliana = int(input("Digite a idade de Juliana: "))

# Solicita a idade de Cris e converte para inteiro
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambas as idades são maiores que 17
pode_entrar = idade_juliana > 17 and idade_cris > 17

# Imprime o resultado
print(pode_entrar)
