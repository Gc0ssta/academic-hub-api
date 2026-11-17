from copy import deepcopy

from armazenamento import carregar_aulas, salvar_aulas
from cadastro import atribuir_ids_microaulas


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
