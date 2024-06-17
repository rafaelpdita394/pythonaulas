# Solicita a distância da entrega e converte para inteiro
distancia = int(input("Digite a distância da entrega (em km): "))

# Solicita o peso do pacote e converte para inteiro
peso = int(input("Digite o peso do pacote (em kg): "))

# Calcula o valor do frete com base na distância
if distancia <= 100:
    frete = peso * 1
elif distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2

# Adiciona a taxa adicional para pacotes com peso superior a 10 kg
if peso > 10:
    frete += 10

# Imprime o valor do frete
print(f"O valor do frete é: R${frete:.2f}")
