def calcula_area_perimetro(dimensoes):
    largura, comprimento = dimensoes
    area = largura * comprimento
    perimetro = 2 * (largura + comprimento)
    return area, perimetro

# Exemplo de uso
largura = 5
comprimento = 7
retorno = calcula_area_perimetro((largura, comprimento))
print(retorno, type(retorno))
