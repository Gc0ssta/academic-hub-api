from datetime import date, timedelta

from calculos import calcular_tempo_video


def gerar_atividades_microaulas_pendentes(
    microaulas: list[dict],
    velocidade: float,
) -> list[dict]:
    """Retorna atividades das microaulas pendentes na ordem recebida.

    Cada atividade contém tipo ("microaula"), titulo e
    tempo_estimado_minutos, calculado na velocidade informada.
    Não modifica os dados recebidos nem inclui revisões.
    """
    if velocidade <= 0:
        raise ValueError("A velocidade deve ser maior que zero.")

    atividades = []

    for microaula in microaulas:
        if type(microaula["concluida"]) is not bool:
            raise TypeError("A conclusão da microaula deve ser um booleano.")

        if microaula["concluida"] is True:
            continue

        tempo_estimado = calcular_tempo_video(
            microaula["duracao_minutos"],
            velocidade,
        )

        atividade = {
            "tipo": "microaula",
            "titulo": microaula["titulo"],
            "tempo_estimado_minutos": tempo_estimado,
        }
        atividades.append(atividade)

    return atividades


def gerar_datas_periodo(
    data_inicio: date,
    data_fim: date,
) -> list[date]:

    if data_fim < data_inicio:
        raise ValueError("A data final nao pode ser menor que a data de inicio")

    datas = []

    data_atual = data_inicio

    while data_atual <= data_fim:
        datas.append(data_atual)
        data_atual += timedelta(days=1)

    return datas

def gerar_disponibilidades_periodo(
    data_inicio: date,
    data_fim: date,
    rotina_semanal: dict[int, float],
    excecoes: dict[date, float],
) -> list[dict]:

    for dia_semana in range(7):
        if dia_semana not in rotina_semanal:
            raise ValueError("A rotina semanal deve informar os sete dias.")

        if rotina_semanal[dia_semana] < 0:
            raise ValueError("A disponibilidade diária não pode ser negativa.")

    for data_excecao in excecoes:
        if excecoes[data_excecao] < 0:
            raise ValueError("A disponibilidade diária não pode ser negativa.")
        
    datas = gerar_datas_periodo(data_inicio, data_fim)
    disponibilidades = []

    for dia in datas:
        dia_semana = dia.weekday()

        if dia in excecoes:
            minutos_disponiveis = excecoes[dia]
        else:
            minutos_disponiveis = rotina_semanal[dia_semana]
            
        disponibilidade = {
            "data": dia,
            "minutos_disponiveis": minutos_disponiveis,
        }
        disponibilidades.append(disponibilidade)

    return disponibilidades
