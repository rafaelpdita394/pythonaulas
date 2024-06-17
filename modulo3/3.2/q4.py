# Solicita a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()

# Solicita os pontos de força e converte para inteiro
forca = int(input("Digite os pontos de força (de 1 a 20): "))

# Solicita os pontos de magia e converte para inteiro
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica se os pontos são consistentes com a classe escolhida
if classe == "guerreiro":
    pontos_consistentes = forca >= 15 and magia <= 10
elif classe == "mago":
    pontos_consistentes = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    pontos_consistentes = 5 < forca <= 15 and 5 < magia <= 15
else:
    pontos_consistentes = False

# Imprime o resultado
print(f"Pontos de atributo consistentes com a classe escolhida: {pontos_consistentes}")
