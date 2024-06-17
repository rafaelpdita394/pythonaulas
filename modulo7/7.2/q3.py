import string

def e_palindromo(frase):
    # Remove espaços, pontuação e converte para minúsculas
    frase_limpa = ''.join([char.lower() for char in frase if char.isalnum()])
    # Verifica se é palíndromo
    return frase_limpa == frase_limpa[::-1]

# Loop principal
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    if e_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
