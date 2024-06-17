# Solicita a idade do usuário e converte para inteiro
idade = int(input("Digite sua idade: "))

# Solicita se o usuário já jogou pelo menos 3 jogos de tabuleiro
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogou_tres_jogos = jogou_tres_jogos == "True"

# Solicita o número de vitórias do usuário e converte para inteiro
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica as condições para ingresso no clube
pode_entrar = (16 <= idade <= 18) and jogou_tres_jogos and (vitorias >= 1)

# Imprime o resultado
print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_entrar}")
