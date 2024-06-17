turmas = [
    {'ações comunitárias', 'futebol', 'música', 'rugby'},
    {'ações comunitárias', 'música', 'rugby', 'teatro'},
    {'música', 'rugby', 'teatro', 'vôlei'},
    {'música', 'vôlei', 'rugby'},
    {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'futebol', 'rugby'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'vôlei'}
]

# Encontrando as atividades comuns a todas as turmas
atividades_comuns = set.intersection(*turmas)

# Exibindo o resultado
print(atividades_comuns)
