import random

def main():
    # Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente
    lista = [random.randint(-10, 10) for _ in range(20)]
    
    print("Original:", lista)
    
    # Encontrar o intervalo que possui a maior quantidade de números negativos
    max_negativos = 0
    intervalo_inicio = 0
    
    for i in range(len(lista) - 1):
        if lista[i] < 0 and lista[i + 1] < 0:
            negativos = 2
            j = i + 2
            while j < len(lista) and lista[j] < 0:
                negativos += 1
                j += 1
            if negativos > max_negativos:
                max_negativos = negativos
                intervalo_inicio = i
    
    # Deletar o intervalo encontrado
    intervalo_fim = intervalo_inicio + max_negativos
    del lista[intervalo_inicio:intervalo_fim]
    
    print("Editada:", lista)

if __name__ == "__main__":
    main()
