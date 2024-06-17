from collections import Counter
## Import de coleção >> from collections import Counter

def resultado_votacao(votos):
    total_votos = Counter()
    
    for sessao in votos:
        total_votos.update(sessao)
    
    total_geral = sum(total_votos.values())
    
    resultado = {}
    for candidato, votos in total_votos.items():
        percentual = (votos / total_geral) * 100
        resultado[candidato] = (votos, round(percentual, 2))
    
    return resultado

# Exemplo de uso:
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)  # Saída esperada: {'candidato_A': (360, 40.31), 'candidato_B': (258, 28.89), 
                # 'candidato_C': (275, 30.79)}
