def avalia_tabuleiro(tabuleiro):
    # Verificação das linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]
    
    # Verificação das diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]
    
    return "Empate"

# Teste a função nos seguintes tabuleiros
tabuleiros = [
    [
        ['X', 'O', 'X'],
        [' ', 'X', 'O'],
        ['O', ' ', 'X']
    ],
    [
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
        ['X', 'O', 'X']
    ],
    [
        [' ', ' ', ' '],
        ['X', ' ', 'O'],
        ['O', 'X', 'X']
    ],
    [
        ['O', 'O', 'O'],
        ['X', ' ', 'X'],
        ['O', 'X', 'X']
    ],
    [
        ['X', 'X', 'O'],
        ['X', ' ', 'O'],
        ['O', 'O', 'X']
    ]
]

for tabuleiro in tabuleiros:
    print("Resultado:", avalia_tabuleiro(tabuleiro))
