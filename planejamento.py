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