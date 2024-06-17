# aula1_questao4.py
from datetime import datetime

def main():
    # Obtém a data e hora atuais
    agora = datetime.now()
    
    # Formata a data e hora
    data_formatada = f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}"
    hora_formatada = f"Hora: {agora.hour:02d}:{agora.minute:02d}"
    
    # Exibe a data e hora formatadas
    print(data_formatada)
    print(hora_formatada)

if __name__ == "__main__":
    main()
