def calcular_media_idades():
    N = int(input("Digite a quantidade de respondentes: "))
    
    # Inicializar a soma das idades
    soma_idades = 0
    
    # Ler as idades e calcular a soma
    for i in range(N):
        idade = int(input(f"Digite a idade do respondente {i+1}: "))
        soma_idades += idade
    
    # Calcular a média das idades
    if N > 0:
        media_idades = soma_idades / N
    else:
        media_idades = 0
    
    print(f"A média das idades dos respondentes é: {media_idades:.2f}")

# Chamada da função para calcular a média de idades
calcular_media_idades()
