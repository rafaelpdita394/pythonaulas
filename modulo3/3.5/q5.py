# Padrões cadastrados no sistema
usuarios = {
    1: (100, 200, 300),
    2: (982, 653, 324),
    3: (110, 220, 330),
    4: (987, 654, 321)
}

# Margem de erro
tolerancia = 10

# Solicita a leitura do padrão de íris
print("Insira o padrão de íris para autenticação.")
atributo1 = int(input("Atributo 1: "))
atributo2 = int(input("Atributo 2: "))
atributo3 = int(input("Atributo 3: "))

# Verifica a autenticação
autenticado = False
for usuario, (a1, a2, a3) in usuarios.items():
    if (abs(a1 - atributo1) <= tolerancia and
        abs(a2 - atributo2) <= tolerancia and
        abs(a3 - atributo3) <= tolerancia):
        autenticado = True
        usuario_autenticado = usuario
        break

# Imprime o resultado da autenticação
if autenticado:
    print(f"Autenticação bem-sucedida! Usuário: {usuario_autenticado}")
else:
    print("Autenticação falhou!")
