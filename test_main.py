from io import StringIO

from main import main, ler_microaula, selecionar_aula, selecionar_indice_microaula

from armazenamento import carregar_aulas

import pytest


def test_terminal_informa_que_atividades_cabem(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\nn\n2\n30\n"
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

def test_terminal_informa_que_atividades_nao_cabem(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\nn\n2\n20\n"
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes não cabem no tempo disponível." in saida

def test_terminal_rejeita_quantidade_de_aulas_zero(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO("0\n")
    monkeypatch.setattr("sys.stdin", entradas)

    main()
    
    saida = capsys.readouterr().out
    
    assert "Não foi possível calcular: A quantidade de aulas deve ser maior que zero." in saida
    assert "Tempo restante: " not in saida

def test_ler_microaula_nao_concluida(monkeypatch):
    entradas = StringIO("Parte 1\n29\nn\n")
    monkeypatch.setattr("sys.stdin", entradas)

    microaula = ler_microaula()

    assert microaula["concluida"] is False
    assert microaula["titulo"] == "Parte 1"
    assert microaula["duracao_minutos"] == 29.0

def test_ler_microaula_concluida(monkeypatch):
    entradas = StringIO("Parte 2\n26\ns\n")
    monkeypatch.setattr("sys.stdin", entradas)

    microaula = ler_microaula()

    assert microaula["concluida"] is True
    assert microaula["titulo"] == "Parte 2"
    assert microaula["duracao_minutos"] == 26.0

def test_ler_microaula_com_duracao_zero(monkeypatch):
    entradas = StringIO("Parte 1\n0\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_microaula()

def test_ler_microaula_com_duracao_negativa(monkeypatch):
    entradas = StringIO("Parte 1\n-1\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_microaula()

def test_ler_microaula_com_concluida_talvez(monkeypatch):
    entradas = StringIO("Parte 1\n29\ntalvez\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_microaula()

def test_terminal_calcula_tempo_pendente_de_duas_aulas(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "2\n"
        "Banco de Dados\nAula 1\n1\n"
        "Parte 1\n26\nn\n"
        "10\n"
        "Progamacao\nAula 2\n1\n"
        "Parte 1\n40\nn\n"
        "5\n"
        "n\n2\n60\n"
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()
    
    saida = capsys.readouterr().out
   
    assert "Tempo restante: 48.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

def test_terminal_reutiliza_aulas_salvas(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\nn\n2\n30\n"
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

    novas_entradas = StringIO("n\n1\n60\n")
    monkeypatch.setattr("sys.stdin", novas_entradas)

    main()

    nova_saida = capsys.readouterr().out

    assert "Quantas aulas deseja informar?" not in nova_saida
    assert "Tempo restante: 36.0 minutos" in nova_saida
    assert "As atividades pendentes cabem no tempo disponível." in nova_saida

def test_selecionar_aula_retorna_segunda_aula(monkeypatch):
        
    aulas = [
        {"disciplina": "Banco de Dados", "titulo": "Aula 1"},
        {"disciplina": "Programação", "titulo": "Aula 2"},
    ]

    entradas = StringIO("2\n")
    monkeypatch.setattr("sys.stdin", entradas)

    aula_selecionada = selecionar_aula(aulas)

    assert aula_selecionada is aulas[1]

def test_selecionar_aula_rejeita_zero(monkeypatch):
        
    aulas = [
        {"disciplina": "Banco de Dados", "titulo": "Aula 1"},
        {"disciplina": "Programação", "titulo": "Aula 2"},
    ]

    entradas = StringIO("0\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        selecionar_aula(aulas)

def test_selecionar_aula_rejeita_numero_acima_do_total(monkeypatch):
        
    aulas = [
        {"disciplina": "Banco de Dados", "titulo": "Aula 1"},
        {"disciplina": "Programação", "titulo": "Aula 2"},
    ]

    entradas = StringIO("3\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        selecionar_aula(aulas)

def test_selecionar_indice_microaula_retorna_segundo_indice(monkeypatch, capsys):

    aula = {
        "microaulas": [
            {"titulo": "Parte 1"},
            {"titulo": "Parte 2"},
        ]
    }
    
    entradas = StringIO("2\n")
    monkeypatch.setattr("sys.stdin", entradas)

    indice = selecionar_indice_microaula(aula)

    assert indice == 1

    saida = capsys.readouterr().out

    assert "1 - Parte 1" in saida
    assert "2 - Parte 2" in saida

def test_selecionar_indice_microaula_rejeita_zero(monkeypatch, capsys):

    aula = {
        "microaulas": [
            {"titulo": "Parte 1"},
            {"titulo": "Parte 2"},
        ]
    }
    
    entradas = StringIO("0\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        selecionar_indice_microaula(aula)

    saida = capsys.readouterr().out

    assert "1 - Parte 1" in saida
    assert "2 - Parte 2" in saida

def test_selecionar_indice_microaula_rejeita_numero_acima_do_total(monkeypatch, capsys):

    aula = {
        "microaulas": [
            {"titulo": "Parte 1"},
            {"titulo": "Parte 2"},
        ]
    }
    
    entradas = StringIO("3\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        selecionar_indice_microaula(aula)

    saida = capsys.readouterr().out

    assert "1 - Parte 1" in saida
    assert "2 - Parte 2" in saida

def test_terminal_marca_microaula_e_salva_progresso(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\nn\n2\n30\n"
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

    novas_entradas = StringIO(
        "s\n"   # Quero marcar uma conclusão.
        "1\n"   # Primeira aula.
        "2\n"   # Segunda microaula.
        "2\n"   # Velocidade dos vídeos.
        "60\n"  # Tempo disponível.
    )
    monkeypatch.setattr("sys.stdin", novas_entradas)

    main()

    nova_saida = capsys.readouterr().out

    assert "Quantas aulas deseja informar?" not in nova_saida
    assert "Tempo restante: 10.0 minutos" in nova_saida
    assert "As atividades pendentes cabem no tempo disponível." in nova_saida

    aulas_salvas = carregar_aulas("aulas.json")
    aula_salva = aulas_salvas[0]

    assert aula_salva["microaulas"][1]["concluida"] is True
    assert aula_salva["tempo_revisao_pendente"] == 10


