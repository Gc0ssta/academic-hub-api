def calcular_tempo_video(duracao_minutos, velocidade):
    if velocidade <= 0:
        raise ValueError("A velocidade deve ser maior que zero.")

    if duracao_minutos <= 0:
        raise ValueError("A duração do video deve ser maior que zero.")
    
    return duracao_minutos / velocidade

def calcular_tempo_aula(duracao_microaula, quantidade_microaulas, velocidade, tempo_revisao):

    if tempo_revisao < 0:
        raise ValueError("O tempo de revisão não pode ser um número negativo")

    if type(quantidade_microaulas) is not int:
        raise TypeError("A quantidade de micro aulas precisa ser um número inteiro")

    if quantidade_microaulas <= 0:
        raise ValueError("A quantidade de micro aulas precisa ser maior que zero")

    tempo_microaula = calcular_tempo_video(duracao_microaula, velocidade)

    tempo_aula = tempo_microaula * quantidade_microaulas

    aula_revisao = tempo_aula + tempo_revisao

    return aula_revisao
