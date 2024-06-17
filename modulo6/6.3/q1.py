def main():
    lista = []
    print("Digite pelo menos 4 valores inteiros (digite 'done' para terminar):")
    
    while len(lista) < 4:
        try:
            valor = input("Digite um número inteiro: ")
            if valor.lower() == 'done' and len(lista) >= 4:
                break
            lista.append(int(valor))
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")
    
    print("Lista original:", lista)
    print("Os 3 primeiros elementos:", lista[:3])
    print("Os 2 últimos elementos:", lista[-2:])
    print("A lista invertida:", lista[::-1])
    print("Elementos de índice par:", lista[0::2])
    print("Elementos de índice ímpar:", lista[1::2])

if __name__ == "__main__":
    main()
