from copy import deepcopy
from datetime import date

from planejamento import (
    gerar_atividades_microaulas_pendentes,
    gerar_datas_periodo,
    gerar_disponibilidades_periodo,
)

import pytest


def test_gerar_atividades_filtra_concluidas_preserva_ordem_e_calcula_tempos():
    microaulas = [
        {"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": True},
        {"id": "micro-2", "titulo": "Parte 2", "duracao_minutos": 40, "concluida": False},
        {"id": "micro-3", "titulo": "Parte 3", "duracao_minutos": 20, "concluida": True},
        {"id": "micro-4", "titulo": "Parte 4", "duracao_minutos": 15, "concluida": False},
    ]

    resultado = gerar_atividades_microaulas_pendentes(microaulas, 2)

    assert resultado == [
        {"microaula_id": "micro-2", "tipo": "microaula", "titulo": "Parte 2", "tempo_estimado_minutos": 20},
        {"microaula_id": "micro-4", "tipo": "microaula", "titulo": "Parte 4", "tempo_estimado_minutos": 7.5},
    ]


@pytest.mark.parametrize("microaulas", [
    [],
    [{"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": True}],
])
def test_gerar_atividades_sem_pendencias_retorna_lista_vazia(microaulas):
    assert gerar_atividades_microaulas_pendentes(microaulas, 2) == []


def test_gerar_atividades_nao_modifica_as_microaulas_recebidas():
    microaulas = [
        {"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": True},
        {"id": "micro-2", "titulo": "Parte 2", "duracao_minutos": 40, "concluida": False},
    ]
    original = deepcopy(microaulas)

    resultado = gerar_atividades_microaulas_pendentes(microaulas, 2)
    resultado[0]["titulo"] = "Título alterado na atividade"

    assert microaulas == original


@pytest.mark.parametrize("velocidade", [0, -1])
@pytest.mark.parametrize("microaulas", [
    [],
    [{"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": True}],
    [{"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": False}],
])
def test_gerar_atividades_rejeita_velocidade_invalida(microaulas, velocidade):
    with pytest.raises(ValueError, match="A velocidade deve ser maior que zero"):
        gerar_atividades_microaulas_pendentes(microaulas, velocidade)


@pytest.mark.parametrize("concluida", [1, "False", None])
def test_gerar_atividades_rejeita_conclusao_nao_booleana(concluida):
    microaulas = [
        {"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": concluida},
    ]

    with pytest.raises(TypeError, match="A conclusão da microaula deve ser um booleano"):
        gerar_atividades_microaulas_pendentes(microaulas, 2)


@pytest.mark.parametrize("duracao", [0, -10])
def test_gerar_atividades_rejeita_duracao_pendente_invalida(duracao):
    microaulas = [
        {"id": "micro-1", "titulo": "Parte 1", "duracao_minutos": duracao, "concluida": False},
    ]

    with pytest.raises(ValueError, match="A duração do video deve ser maior que zero"):
        gerar_atividades_microaulas_pendentes(microaulas, 2)


def test_gerar_atividades_preserva_vinculo_com_titulos_iguais_e_apos_conclusao():
    microaulas = [
        {"id": "micro-a", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": False},
        {"id": "micro-b", "titulo": "Parte 1", "duracao_minutos": 30, "concluida": False},
    ]

    atividades = gerar_atividades_microaulas_pendentes(microaulas, 2)

    assert atividades == [
        {"microaula_id": "micro-a", "tipo": "microaula", "titulo": "Parte 1", "tempo_estimado_minutos": 15},
        {"microaula_id": "micro-b", "tipo": "microaula", "titulo": "Parte 1", "tempo_estimado_minutos": 15},
    ]

    microaulas[0]["concluida"] = True
    novo_resultado = gerar_atividades_microaulas_pendentes(microaulas, 1)

    assert novo_resultado == [
        {"microaula_id": "micro-b", "tipo": "microaula", "titulo": "Parte 1", "tempo_estimado_minutos": 30},
    ]
    assert microaulas[0]["id"] == "micro-a"
    assert len(microaulas) == 2


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
