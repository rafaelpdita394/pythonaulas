import csv

# Caminho para o arquivo CSV baixado do Kaggle
file_path = 'spotify-2023.csv'

# Dicionário para armazenar as músicas mais tocadas por ano
top_songs_by_year = {}

# Leitura do arquivo CSV
with open(file_path, 'r', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pular cabeçalho

    for row in reader:
        # Extrair informações relevantes
        track_name = row[0].strip()
        artists = row[1].strip()
        artist_count = int(row[2].strip())
        released_year = int(row[3].strip())

        # Ignorar músicas com artistas listados entre aspas
        if '"' in artists:
            continue

        # Considerar apenas músicas lançadas entre 2012 e 2022
        if 2012 <= released_year <= 2022:
            streams = int(row[8].strip())

            # Atualizar as músicas mais tocadas por ano
            if released_year not in top_songs_by_year:
                top_songs_by_year[released_year] = []

            top_songs_by_year[released_year].append([track_name, artists, released_year, streams])

# Lista para armazenar as músicas mais tocadas de cada ano (2012-2022)
top_songs_list = []

# Selecionar as músicas mais tocadas de cada ano
for year in range(2012, 2023):
    if year in top_songs_by_year:
        # Encontrar a música com o maior número de streams para o ano atual
        top_song = max(top_songs_by_year[year], key=lambda x: x[3])
        top_songs_list.append([top_song[0], top_song[1], top_song[2], top_song[3]])

# Imprimir a lista de músicas mais tocadas
print(top_songs_list)
