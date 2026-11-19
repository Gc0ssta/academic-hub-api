from progresso import marcar_microaula_concluida, marcar_revisao_concluida

import pytest

def test_marcar_microaula_concluida_indice_1():
    aulas = {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {
                    "titulo": "Parte 1",
                    "duracao_minutos": 29,
                    "concluida": False,
                },
                {
                    "titulo": "Parte 2",
                    "duracao_minutos": 26,
                    "concluida": False,
                },
            ],
            "revisao": {"id": "rev-teste", "duracao_minutos": 10, "concluida": False},
        }

    marcar_microaula_concluida(aulas, 1)

    assert aulas["microaulas"][1]["concluida"] is True
    assert aulas["microaulas"][0]["concluida"] is False
    assert aulas["microaulas"][0]["duracao_minutos"] == 29
    assert aulas["microaulas"][1]["duracao_minutos"] == 26
    assert aulas["revisao"] == {"id": "rev-teste", "duracao_minutos": 10, "concluida": False}

def test_rejeita_indice_negativo():

    aulas = {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {
                    "titulo": "Parte 1",
                    "duracao_minutos": 29,
                    "concluida": False,
                },
                {
                    "titulo": "Parte 2",
                    "duracao_minutos": 26,
                    "concluida": False,
                },
            ],
            "revisao": {"id": "rev-teste", "duracao_minutos": 10, "concluida": False},
        }
        
    with pytest.raises(IndexError):
        marcar_microaula_concluida(aulas, -1)

    assert aulas["microaulas"][0]["concluida"] is False
    assert aulas["microaulas"][1]["concluida"] is False

def test_rejeita_indice_fora_da_lista():

    aulas = {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {
                    "titulo": "Parte 1",
                    "duracao_minutos": 29,
                    "concluida": False,
                },
                {
                    "titulo": "Parte 2",
                    "duracao_minutos": 26,
                    "concluida": False,
                },
            ],
            "revisao": {"id": "rev-teste", "duracao_minutos": 10, "concluida": False},
        }

    with pytest.raises(IndexError):
        marcar_microaula_concluida(aulas, 2)

    assert aulas["microaulas"][0]["concluida"] is False
    assert aulas["microaulas"][1]["concluida"] is False

def test_rejeita_indice_decimal():

    aulas = {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {
                    "titulo": "Parte 1",
                    "duracao_minutos": 29,
                    "concluida": False,
                },
                {
                    "titulo": "Parte 2",
                    "duracao_minutos": 26,
                    "concluida": False,
                },
            ],
            "revisao": {"id": "rev-teste", "duracao_minutos": 10, "concluida": False},
        }

    with pytest.raises(TypeError):
        marcar_microaula_concluida(aulas, 1.5)

    assert aulas["microaulas"][0]["concluida"] is False
    assert aulas["microaulas"][1]["concluida"] is False

def test_concluir_revisao_permitida():
    aulas = {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {
                    "titulo": "Parte 1",
                    "duracao_minutos": 29,
                    "concluida": True,
                },
                {
                    "titulo": "Parte 2",
                    "duracao_minutos": 26,
                    "concluida": True,
                },
            ],
            "revisao": {"id": "rev-teste", "duracao_minutos": 10, "concluida": False},
        }

    marcar_revisao_concluida(aulas)

    assert aulas["revisao"] == {"id": "rev-teste", "duracao_minutos": 10, "concluida": True}
    assert aulas["microaulas"][0]["concluida"] is True
    assert aulas["microaulas"][1]["concluida"] is True

def test_concluir_revisao_bloqueada():
    aulas = {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {
                    "titulo": "Parte 1",
                    "duracao_minutos": 29,
                    "concluida": True,
                },
                {
                    "titulo": "Parte 2",
                    "duracao_minutos": 26,
                    "concluida": False,
                },
            ],
            "revisao": {"id": "rev-teste", "duracao_minutos": 10, "concluida": False},
        }

    with pytest.raises(ValueError):
        marcar_revisao_concluida(aulas)

    assert aulas["revisao"] == {"id": "rev-teste", "duracao_minutos": 10, "concluida": False}
    assert aulas["microaulas"][0]["concluida"] is True
    assert aulas["microaulas"][1]["concluida"] is False