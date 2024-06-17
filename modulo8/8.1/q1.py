frase = "O rato roeu a roupa do Robson"

# Transformando a frase em um set para obter caracteres únicos
caracteres_unicos = set(frase)

# Convertendo para uma lista para ordenar e eliminando espaços em branco
caracteres_unicos = sorted([char for char in caracteres_unicos if char != ' '])

# Exibindo o resultado
print(caracteres_unicos)
