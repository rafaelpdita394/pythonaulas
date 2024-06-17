def calcular_experimentos():
    N = int(input("Digite a quantidade de experimentos registrados: "))
    
    total_cobaias = 0
    total_sapos = 0
    total_ratos = 0
    total_coelhos = 0
    
    # Processar cada experimento
    for i in range(N):
        entrada = input(f"Digite a quantidade e o tipo de cobaias do experimento {i+1} (ex: 10 C): ")
        partes = entrada.split()
        
        if len(partes) != 2:
            continue
        
        quantidade = int(partes[0])
        tipo = partes[1].upper()
        
        total_cobaias += quantidade
        
        if tipo == 'S':
            total_sapos += quantidade
        elif tipo == 'R':
            total_ratos += quantidade
        elif tipo == 'C':
            total_coelhos += quantidade
    
    # Calcular percentuais
    if total_cobaias > 0:
        percentual_sapos = (total_sapos / total_cobaias) * 100
        percentual_ratos = (total_ratos / total_cobaias) * 100
        percentual_coelhos = (total_coelhos / total_cobaias) * 100
    else:
        percentual_sapos = 0
        percentual_ratos = 0
        percentual_coelhos = 0
    
    # Imprimir resultados
    print(f"Total: {total_cobaias} cobaias")
    print(f"Total de sapos: {total_sapos}")
    print(f"Total de ratos: {total_ratos}")
    print(f"Total de coelhos: {total_coelhos}")
    print(f"Percentual de sapos: {percentual_sapos:.2f}%")
    print(f"Percentual de ratos: {percentual_ratos:.2f}%")
    print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")

# Chamada da função para calcular os experimentos
calcular_experimentos()
