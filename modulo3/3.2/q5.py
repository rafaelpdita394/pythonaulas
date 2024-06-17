# Solicita o gênero do usuário
genero = input("Digite seu gênero (M/F): ").strip().upper()

# Solicita a idade do usuário e converte para inteiro
idade = int(input("Digite sua idade: "))

# Solicita o tempo de serviço do usuário e converte para inteiro
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verifica as condições para aposentadoria
if genero == "F":
    pode_aposentar = idade > 60 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)
elif genero == "M":
    pode_aposentar = idade > 65 or tempo_servico >= 30 or (idade >= 65 and tempo_servico >= 25)
else:
    pode_aposentar = False

# Imprime o resultado
print(pode_aposentar)
