from calculos import calcular_microaulas_pendentes, calcular_tempo_restante_aula, cabe_no_tempo

try:
    quantidade_total = int(input("Quantas microaulas a aula possui? "))
    quantidade_concluida = int(input("Quantas você já concluiu? "))
    duracao_microaula = float(input("Quanto tempo dura a MicroAula em minutos? "))
    velocidade_microaula = float(input("Qual velocidade do video? "))
    tempo_revisao = float(input("Quantos minutos de revisão ainda faltam? "))
    tempo_disponivel = float(input("Quantos minutos você tem disponíveis? "))

    result_microaulas_pendentes = calcular_microaulas_pendentes(
        quantidade_total, 
        quantidade_concluida
    )
    
    tempo_restante = calcular_tempo_restante_aula(
        duracao_microaula, 
        quantidade_total, 
        quantidade_concluida, 
        velocidade_microaula, 
        tempo_revisao
    )

    atividade_cabe = cabe_no_tempo(
        tempo_restante, 
        tempo_disponivel
    )


except ValueError as erro:
    print("Não foi possível calcular:", erro)
else:
    print('faltam:', result_microaulas_pendentes, 'MicroAulas!')
    print("Tempo restante:", tempo_restante, "minutos")
    
    if atividade_cabe:
        print("As atividades pendentes cabem no tempo disponível.")
    else:
        print("As atividades pendentes não cabem no tempo disponível.")





