def coletar_dados():
    lista_pessoas = []
    while True:
        nome = input("Digite o nome (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        idade = int(input("Digite a idade: "))
        lista_pessoas.append((nome, idade))
    return lista_pessoas

def separar_idades(lista_pessoas):
    menores = tuple(nome for nome, idade in lista_pessoas if idade < 18)
    maiores = tuple(nome for nome, idade in lista_pessoas if idade >= 18)
    return menores, maiores

# Coleta de dados
lista_pessoas = coletar_dados()

# Separação de menores e maiores de idade
menores, maiores = separar_idades(lista_pessoas)

# Exibição dos resultados
print(f"Menores de idade: {menores}")
print(f"Maiores de idade: {maiores}")
