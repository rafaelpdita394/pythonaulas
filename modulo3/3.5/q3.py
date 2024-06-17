# Solicita a pontuação do jogador e converte para inteiro
pontuacao = int(input("Digite a pontuação: "))

# Atribui a classificação com base na pontuação
if pontuacao >= 90:
    classificacao = "Excelente"
elif pontuacao >= 80:
    classificacao = "Bom"
elif pontuacao >= 70:
    classificacao = "Regular"
else:
    classificacao = "Insatisfatório"

# Imprime a classificação
print(f"Classificação: {classificacao}")
