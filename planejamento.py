from datetime import date, timedelta


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