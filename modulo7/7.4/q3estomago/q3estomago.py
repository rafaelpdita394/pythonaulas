# Caminho para o arquivo estomago.txt no seu computador
file_path = 'estomago.txt'  # Substitua com o caminho correto

# 1. Abrindo o arquivo para leitura
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. Imprimindo as primeiras 25 linhas
print("\nPrimeiras 25 linhas:")
for line in lines[:25]:
    print(line.strip())  # strip() para remover espaços em branco extras

# 3. Número de linhas do arquivo
num_lines = len(lines)
print(f"\nNúmero total de linhas no arquivo: {num_lines}")

# 4. Linha com maior número de caracteres
max_length_line = max(lines, key=len).strip()
max_length = len(max_length_line)
print(f"\nLinha com maior número de caracteres ({max_length} caracteres):\n{max_length_line}")

# 5. Contagem de menções aos nomes "Nonato" e "Íria"
count_nonato = 0
count_iria = 0

for line in lines:
    # Convertendo a linha para minúsculas para fazer a contagem sem distinção de maiúsculas/minúsculas
    lower_line = line.lower()

    # Contagem de "Nonato"
    count_nonato += lower_line.count("nonato")

    # Contagem de "Íria"
    count_iria += lower_line.count("íria")

print(f"\nNúmero de menções a 'Nonato': {count_nonato}")
print(f"Número de menções a 'Íria': {count_iria}")
