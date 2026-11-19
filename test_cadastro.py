from copy import deepcopy

from armazenamento import carregar_aulas, salvar_aulas
from cadastro import atribuir_ids_microaulas, criar_revisao, adaptar_revisao_antiga

import pytest


def test_adaptar_revisao_pendente_preserva_cadastro_e_nao_repete_adaptacao():
    aula = {
        "titulo": "Aula 1",
        "microaulas": [{"id": "micro-1", "concluida": True}],
        "tempo_revisao_pendente": 12.5,
    }
    adaptar_revisao_antiga(aula)

    assert "tempo_revisao_pendente" not in aula
    assert aula["revisao"]["duracao_minutos"] == 12.5
    assert aula["revisao"]["concluida"] is False
    assert isinstance(aula["revisao"]["id"], str)
    assert aula["revisao"]["id"] != ""
    assert aula["microaulas"] == [{"id": "micro-1", "concluida": True}]
    assert aula["titulo"] == "Aula 1"
    adaptada = deepcopy(aula)

    adaptar_revisao_antiga(aula, duracao_original=99)

    assert aula == adaptada


def test_adaptar_revisao_com_zero_usa_duracao_informada_e_preserva_conclusao():
    aula = {"tempo_revisao_pendente": 0}

    adaptar_revisao_antiga(aula, duracao_original=15)

    assert aula["revisao"]["duracao_minutos"] == 15
    assert aula["revisao"]["concluida"] is True
    assert "tempo_revisao_pendente" not in aula


@pytest.mark.parametrize("duracao", [None, 0, -10])
def test_adaptar_revisao_com_zero_rejeita_duracao_ausente_ou_invalida(duracao):
    aula = {"tempo_revisao_pendente": 0}

    with pytest.raises(ValueError):
        adaptar_revisao_antiga(aula, duracao)

    assert aula == {"tempo_revisao_pendente": 0}


def test_adaptar_revisao_rejeita_minutos_antigos_negativos_sem_alterar():
    aula = {"tempo_revisao_pendente": -5}
    with pytest.raises(ValueError, match="não pode ser negativo"):
        adaptar_revisao_antiga(aula)
    assert aula == {"tempo_revisao_pendente": -5}


@pytest.mark.parametrize("duracao", [0, -1])
def test_criar_revisao_rejeita_duracao_nao_positiva(duracao):
    with pytest.raises(ValueError, match="maior que zero"):
        criar_revisao(duracao)


@pytest.mark.parametrize("concluida", [1, "False", None])
def test_criar_revisao_rejeita_conclusao_nao_booleana(concluida):
    with pytest.raises(TypeError, match="booleano"):
        criar_revisao(10, concluida)


def test_atribuir_ids_preserva_dados_e_identifica_microaulas_de_aulas_diferentes():
    aulas = [
        {
            "disciplina": "Banco de Dados",
            "titulo": "Aula 1",
            "microaulas": [
                {"titulo": "Parte 1", "duracao_minutos": 30, "concluida": True},
                {"titulo": "Parte 2", "duracao_minutos": 20, "concluida": False},
            ],
            "tempo_revisao_pendente": 10,
        },
        {
            "disciplina": "Programação",
            "titulo": "Aula 1",
            "microaulas": [
                {"titulo": "Parte 1", "duracao_minutos": 25, "concluida": False},
            ],
            "tempo_revisao_pendente": 10,
        },
    ]
    original = deepcopy(aulas)

    atribuir_ids_microaulas(aulas)

    ids = []
    sem_ids = deepcopy(aulas)
    for aula in sem_ids:
        for microaula in aula["microaulas"]:
            identificador = microaula.pop("id")
            assert isinstance(identificador, str)
            assert identificador != ""
            assert identificador not in ids
            ids.append(identificador)
    assert sem_ids == original


def test_atribuir_ids_preserva_existentes_ao_repetir_renomear_e_inserir_microaula():
    existente = {
        "id": "micro-existente",
        "titulo": "Parte 1",
        "duracao_minutos": 30,
        "concluida": True,
    }
    nova = {"titulo": "Parte 2", "duracao_minutos": 20, "concluida": False}
    aulas = [{"microaulas": [existente, nova]}]
    atribuir_ids_microaulas(aulas)
    id_nova = nova["id"]

    existente["titulo"] = "Introdução ao SQL"
    inserida = {"titulo": "Parte extra", "duracao_minutos": 10, "concluida": False}
    aulas[0]["microaulas"].insert(0, inserida)
    atribuir_ids_microaulas(aulas)

    assert existente["id"] == "micro-existente"
    assert nova["id"] == id_nova
    assert inserida["id"] not in ["micro-existente", id_nova]


def test_ids_permanecem_apos_salvar_carregar_e_atribuir_novamente(tmp_path):
    aulas = [{"microaulas": [
        {"titulo": "Parte 1", "duracao_minutos": 30, "concluida": False},
    ]}]
    caminho = str(tmp_path / "aulas.json")
    atribuir_ids_microaulas(aulas)
    salvar_aulas(aulas, caminho)

    carregadas = carregar_aulas(caminho)
    atribuir_ids_microaulas(carregadas)

    assert carregadas == aulas


def test_atribuir_ids_aceita_lista_vazia():
    aulas = []
    atribuir_ids_microaulas(aulas)
    assert aulas == []
