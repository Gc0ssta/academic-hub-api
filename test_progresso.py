from progresso import marcar_microaula_concluida

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
            "tempo_revisao_pendente": 10,
        }

    marcar_microaula_concluida(aulas, 1)

    assert aulas["microaulas"][1]["concluida"] is True
    assert aulas["microaulas"][0]["concluida"] is False
    assert aulas["microaulas"][0]["duracao_minutos"] == 29
    assert aulas["microaulas"][1]["duracao_minutos"] == 26
    assert aulas["tempo_revisao_pendente"] == 10

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
            "tempo_revisao_pendente": 10,
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
            "tempo_revisao_pendente": 10,
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
            "tempo_revisao_pendente": 10,
        }

    with pytest.raises(TypeError):
        marcar_microaula_concluida(aulas, 1.5)

    assert aulas["microaulas"][0]["concluida"] is False
    assert aulas["microaulas"][1]["concluida"] is False