# Questão 4
print("Questão 4:")
N = int(input("Digite a quantidade de jogos do Atlético MG: "))

vitorias = 0
empates = 0
derrotas = 0
pontuacao = 0

for _ in range(N):
    gols_galo, gols_oponente = map(int, input().split())
    if gols_galo > gols_oponente:
        vitorias += 1
        pontuacao += 3
    elif gols_galo == gols_oponente:
        empates += 1
        pontuacao += 1
    else:
        derrotas += 1

print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontuacao}")
