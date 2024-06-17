# aula2_questao4.py

# Definindo a distância em quilômetros e convertendo para metros
distancia_km = 42.195
distancia_metros = distancia_km * 1000  # convertendo para metros

# Definindo o tempo em horas e convertendo para segundos
tempo_horas = 3
tempo_segundos = tempo_horas * 3600  # convertendo para segundos

# Calculando a velocidade média em m/s
velocidade_media = distancia_metros / tempo_segundos

# Imprimindo o resultado
print(f"Velocidade média necessária para completar a Maratona Internacional de São Silvestre: {velocidade_media:.2f} m/s")
