# Função para intercalar duas listas
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho_minimo = min(len(lista1), len(lista2))
    
    for i in range(tamanho_minimo):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    lista_intercalada.extend(lista1[tamanho_minimo:])
    lista_intercalada.extend(lista2[tamanho_minimo:])
    
    return lista_intercalada

# Receber duas listas do usuário
def receber_lista(tamanho):
    lista = []
    for i in range(tamanho):
        elemento = int(input(f"Digite o {i+1}º elemento: "))
        lista.append(elemento)
    return lista

# Programa principal
def main():
    tamanho_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
    print(f"Digite os {tamanho_lista1} elementos da lista 1:")
    lista1 = receber_lista(tamanho_lista1)
    
    tamanho_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
    print(f"Digite os {tamanho_lista2} elementos da lista 2:")
    lista2 = receber_lista(tamanho_lista2)
    
    lista_intercalada = intercalar_listas(lista1, lista2)
    
    print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))

if __name__ == "__main__":
    main()
