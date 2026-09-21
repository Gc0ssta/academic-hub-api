def calcular_tempo_video(duracao_minutos, velocidade):
    if velocidade <= 0:
        raise ValueError("A velocidade deve ser maior que zero.")

    if duracao_minutos <= 0:
        raise ValueError("A duração do video deve ser maior que zero.")
    
    return duracao_minutos / velocidade
