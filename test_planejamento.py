from datetime import date

from planejamento import gerar_datas_periodo

import pytest


def test_gerar_datas_periodo_inclui_inicio_e_fim():
    resultado = gerar_datas_periodo(
        data_inicio=date(2026, 10, 15),
        data_fim=date(2026, 10, 17),
    )

    assert resultado == [
        date(2026, 10, 15),
        date(2026, 10, 16),
        date(2026, 10, 17),
    ]

def test_gerar_datas_periodo_com_uma_data():
    resultado = gerar_datas_periodo(
        data_inicio=date(2026, 10, 15),
        data_fim=date(2026, 10, 15),
    )

    assert resultado == [date(2026, 10, 15)]

def test_gerar_datas_periodo_data_inicio_maior_que_a_data_final():

    with pytest.raises(ValueError):
        gerar_datas_periodo(
            data_inicio=date(2026, 10, 17),
            data_fim=date(2026, 10, 15),
        )

def test_gerar_datas_periodo_atravesar_mudanca_mes():
    resultado = gerar_datas_periodo(
        data_inicio=date(2026, 10, 31),
        data_fim=date(2026, 11, 2),
    )

    assert resultado == [
        date(2026, 10, 31),
        date(2026, 11, 1),
        date(2026, 11, 2),
    ]