from armazenamento import salvar_aulas, carregar_aulas

import json
import pytest

def test_salvar_e_carregar_aulas_preserva_os_dados(tmp_path):

    aulas = [
    {
        "disciplina": "Programação",
        "titulo": "Aula 1",
        "microaulas": [
            {
                "titulo": "Parte 1",
                "duracao_minutos": 30,
                "concluida": False,
            }
        ],
        "tempo_revisao_pendente": 10,
    }
]   

    caminho = str(tmp_path / "aulas.json")

    salvar_aulas(aulas, caminho)
    aulas_carregadas = carregar_aulas(caminho)

    assert aulas_carregadas == aulas

def test_carregar_aulas_sem_arquivo_retorna_lista_vazia(tmp_path):
    caminho = str(tmp_path / "inexistente.json")

    aulas = carregar_aulas(caminho)

    assert aulas == []

def test_carregar_aulas_rejeita_json_invalido(tmp_path):
    caminho = str(tmp_path / "aulas.json")

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("{")

    with pytest.raises(json.JSONDecodeError):
        carregar_aulas(caminho)
