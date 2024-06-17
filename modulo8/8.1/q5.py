def checa_panagrama(frase):
    # Set de todas as letras do alfabeto
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    
    # Removendo espaços e transformando a frase para minúsculas
    frase = frase.replace(' ', '').lower()
    
    # Set de caracteres únicos na frase
    caracteres_frase = set(frase)
    
    # Verificando se todos os caracteres do alfabeto estão presentes na frase
    return alfabeto.issubset(caracteres_frase)

# Testando a função
frase1 = "The quick brown fox jumps over the lazy dog"
frase2 = "Python é uma linguagem de programação"

print(checa_panagrama(frase1))  # Saída esperada: True (É um panagrama)
print(checa_panagrama(frase2))  # Saída esperada: False (Não é um panagrama)
