from datetime import date

from planejamento import (
    gerar_datas_periodo,
    gerar_disponibilidades_periodo,
)

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

def test_gerar_disponibilidades_periodo_aplica_rotina_semanal():
    rotina_semanal = {
        0: 60,
        1: 60,
        2: 80,
        3: 60,
        4: 30,
        5: 120,
        6: 0,
    }

    resultado = gerar_disponibilidades_periodo(
            data_inicio=date(2026, 10, 16),
            data_fim=date(2026, 10, 18),
            rotina_semanal=rotina_semanal,
            excecoes={},
        )

    assert resultado == [
        {"data": date(2026, 10, 16), "minutos_disponiveis": 30},
        {"data": date(2026, 10, 17), "minutos_disponiveis": 120},
        {"data": date(2026, 10, 18), "minutos_disponiveis": 0},
    ]

def test_gerar_disponibilidades_periodo_sem_domingo():
    rotina_semanal = {
        0: 60,
        1: 60,
        2: 80,
        3: 60,
        4: 30,
        5: 120,
    }
    with pytest.raises(ValueError):
        gerar_disponibilidades_periodo(
            data_inicio=date(2026, 10, 16),
            data_fim=date(2026, 10, 18),
            rotina_semanal=rotina_semanal,
            excecoes={},
        )

def test_gerar_disponibilidades_periodo_disponibilidade_negativa():
    rotina_semanal = {
        0: -10,
        1: 60,
        2: 80,
        3: 60,
        4: 30,
        5: 120,
        6: 0,
    }
    with pytest.raises(ValueError):
        gerar_disponibilidades_periodo(
            data_inicio=date(2026, 10, 16),
            data_fim=date(2026, 10, 18),
            rotina_semanal=rotina_semanal,
            excecoes={},
        )

def test_gerar_disponibilidades_periodo_sem_sexta():
    rotina_semanal = {
        0: 60,
        1: 60,
        2: 80,
        3: 60,
        5: 120,
        6: 0,
    }
    with pytest.raises(ValueError):
        gerar_disponibilidades_periodo(
            data_inicio=date(2026, 10, 16),
            data_fim=date(2026, 10, 18),
            rotina_semanal=rotina_semanal,
            excecoes={},
        )

def test_gerar_disponibilidades_periodo_aplica_excecao_zero():
    rotina_semanal = {
        0: 60,
        1: 60,
        2: 60,
        4: 60,
        3: 60,
        5: 120,
        6: 120,
    }

    resultado = gerar_disponibilidades_periodo(
        data_inicio=date(2026, 10, 17),
        data_fim=date(2026, 10, 18),
        rotina_semanal=rotina_semanal,
        excecoes = {date(2026, 10, 17): 0,},
    )

    assert resultado == [
        {"data": date(2026, 10, 17), "minutos_disponiveis": 0},
        {"data": date(2026, 10, 18), "minutos_disponiveis": 120},
    ]   

    assert rotina_semanal[5] == 120

def test_gerar_disponibilidades_periodo_rejeicao_disponibilidade_negativa():
    rotina_semanal = {
        0: 60,
        1: 60,
        2: 60,
        4: 60,
        3: 60,
        5: 120,
        6: 120,
    }
    with pytest.raises(ValueError):
        gerar_disponibilidades_periodo(
            data_inicio=date(2026, 10, 17),
            data_fim=date(2026, 10, 18),
            rotina_semanal=rotina_semanal,
            excecoes = {date(2026, 10, 17): -10,},
        )

def test_gerar_disponibilidades_periodo_aplica_excecao_minutos():
    rotina_semanal = {
        0: 60,
        1: 60,
        2: 60,
        4: 60,
        3: 60,
        5: 120,
        6: 120,
    }

    resultado = gerar_disponibilidades_periodo(
        data_inicio=date(2026, 10, 17),
        data_fim=date(2026, 10, 18),
        rotina_semanal=rotina_semanal,
        excecoes = {date(2026, 10, 17): 30,},
    )

    assert resultado == [
        {"data": date(2026, 10, 17), "minutos_disponiveis": 30},
        {"data": date(2026, 10, 18), "minutos_disponiveis": 120},
    ]   

    assert rotina_semanal[5] == 120