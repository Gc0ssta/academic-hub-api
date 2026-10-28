from io import StringIO

from main import (
    main, 
    ler_microaula, 
    selecionar_aula, 
    selecionar_indice_microaula, 
    ler_data,
    ler_rotina_semanal,
    ler_excecoes
)

from armazenamento import carregar_aulas, salvar_aulas

import pytest

from datetime import date

def test_terminal_preserva_conclusao_apos_data_invalida(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    aulas = [{
        "disciplina": "Banco de Dados",
        "titulo": "Aula 1",
        "microaulas": [
            {"titulo": "Parte 1", "duracao_minutos": 29, "concluida": False},
            {"titulo": "Parte 2", "duracao_minutos": 26, "concluida": False},
        ],
        "tempo_revisao_pendente": 10,
    }]
    salvar_aulas(aulas, "aulas.json")
    entradas = StringIO(
        "1\n"           # Marcar uma microaula como concluída.
        "1\n"           # Primeira aula.
        "2\n"           # Segunda microaula.
        "2\n"           # Velocidade dos vídeos.
        "2026-02-30\n"  # Data inicial inexistente.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out
    assert "Não foi possível calcular:" in saida
    assert "Tempo restante:" not in saida

    aula_salva = carregar_aulas("aulas.json")[0]
    assert aula_salva["microaulas"][1]["concluida"] is True
    assert aula_salva["microaulas"][0]["concluida"] is False
    assert aula_salva["tempo_revisao_pendente"] == 10


def test_terminal_preserva_cadastro_apos_data_invalida(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"                     # Uma aula nova.
        "Banco de Dados\nAula 1\n1\n"
        "Parte 1\n30\nn\n10\n"
        "0\n"                     # Apenas calcular.
        "2\n"                     # Velocidade dos vídeos.
        "2026-02-30\n"            # Data inexistente.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out
    assert "Não foi possível calcular:" in saida
    assert "Tempo restante:" not in saida
    assert carregar_aulas("aulas.json") == [{
        "disciplina": "Banco de Dados",
        "titulo": "Aula 1",
        "microaulas": [
            {"titulo": "Parte 1", "duracao_minutos": 30, "concluida": False},
        ],
        "tempo_revisao_pendente": 10,
    }]


def test_terminal_preserva_revisao_concluida_apos_data_invalida(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    aulas = [{
        "disciplina": "Banco de Dados",
        "titulo": "Aula 1",
        "microaulas": [
            {"titulo": "Parte 1", "duracao_minutos": 30, "concluida": True},
        ],
        "tempo_revisao_pendente": 10,
    }]
    salvar_aulas(aulas, "aulas.json")
    entradas = StringIO("2\n1\n2\n2026-02-30\n")
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out
    assert "Não foi possível calcular:" in saida
    assert "Tempo restante:" not in saida
    aula_salva = carregar_aulas("aulas.json")[0]
    assert aula_salva["tempo_revisao_pendente"] == 0
    assert aula_salva["microaulas"] == aulas[0]["microaulas"]


def test_terminal_informa_que_atividades_cabem(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida
    assert "Tempo disponível no período: 30.0 minutos" in saida

def test_terminal_informa_que_atividades_nao_cabem(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "20\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes não cabem no tempo disponível." in saida
    assert "Tempo disponível no período: 20.0 minutos" in saida

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
        "5\n"           # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "60\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    
    monkeypatch.setattr("sys.stdin", entradas)

    main()
    
    saida = capsys.readouterr().out
   
    assert "Tempo restante: 48.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida
    assert "Tempo disponível no período: 60.0 minutos" in saida

def test_terminal_reutiliza_aulas_salvas(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )

    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

    novas_entradas = StringIO(
        "0\n"           # Apenas calcular.
        "1\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial.
        "2026-10-19\n"  # Data final.
        "60\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
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
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

    novas_entradas = StringIO(
        "1\n"   # Quero marcar uma conclusão.
        "1\n"   # Primeira aula.
        "2\n"   # Segunda microaula.
        "2\n"   # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial.
        "2026-10-19\n"  # Data final.
        "60\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
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

def test_terminal_conclui_revisao_e_salva_progresso(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\ns\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 10.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

    novas_entradas = StringIO(
        "2\n"   # Concluir revisão.
        "1\n"   # Primeira aula.
        "2\n"   # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial.
        "2026-10-19\n"  # Data final.
        "60\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", novas_entradas)

    main()

    nova_saida = capsys.readouterr().out

    assert "Quantas aulas deseja informar?" not in nova_saida
    assert "Tempo restante: 0.0 minutos" in nova_saida
    assert "As atividades pendentes cabem no tempo disponível." in nova_saida

    aulas_salvas = carregar_aulas("aulas.json")
    aula_salva = aulas_salvas[0]

    assert aula_salva["tempo_revisao_pendente"] == 0
    assert aula_salva["microaulas"][0]["concluida"] is True
    assert aula_salva["microaulas"][1]["concluida"] is True

def test_terminal_bloqueia_revisao_com_microaula_pendente(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

    novas_entradas = StringIO(
        "2\n"   # Tentar concluir revisão.
        "1\n"   # Primeira aula.
    )
    monkeypatch.setattr("sys.stdin", novas_entradas)

    main()

    nova_saida = capsys.readouterr().out

    assert "Quantas aulas deseja informar?" not in nova_saida
    assert "Não foi possível calcular: Ainda ha videos pendentes a serem concluidos" in nova_saida
    assert "Tempo restante:" not in nova_saida

    aulas_salvas = carregar_aulas("aulas.json")
    aula_salva = aulas_salvas[0]

    assert aula_salva["tempo_revisao_pendente"] == 10
    assert aula_salva["microaulas"][0]["concluida"] is True
    assert aula_salva["microaulas"][1]["concluida"] is False

def test_terminal_soma_disponibilidade_de_varios_dias(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial.
        "2026-10-21\n"  # Data final.
        "10\n"          # Segunda.
        "0\n"           # Terça.
        "20\n"          # Quarta.
        "60\n"          # Quinta.
        "60\n"          # Sexta.
        "120\n"          # Sabado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida
    assert "Tempo disponível no período: 30.0 minutos" in saida

def test_ler_data_valida(monkeypatch):

    entradas = StringIO("2026-10-18\n")
    monkeypatch.setattr("sys.stdin", entradas)

    saida = ler_data("Informe uma data (AAAA-MM-DD): ")

    assert saida == date(2026, 10, 18)

def test_ler_data_rejeita_data_inexistente(monkeypatch):

    entradas = StringIO("2026-02-30\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_data("Informe uma data (AAAA-MM-DD): ")

def test_ler_data_rejeita_texto_invalido(monkeypatch):

    entradas = StringIO("abc\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_data("Informe uma data (AAAA-MM-DD): ")

def test_ler_rotina_semanal_aceita_zero_e_minutos_decimais(monkeypatch):
    entradas = StringIO("60\n45\n80\n30.5\n90\n120\n0\n")
    monkeypatch.setattr("sys.stdin", entradas)

    saida = ler_rotina_semanal()

    assert saida == {
                0: 60,
                1: 45,
                2: 80,
                3: 30.5,
                4: 90,
                5: 120,
                6: 0,
            }

def test_ler_rotina_semanal_rejeita_minutos_negativos(monkeypatch):

    entradas = StringIO("60\n-10\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_rotina_semanal()

def test_ler_rotina_semanal_rejeita_texto_invalido(monkeypatch):

    entradas = StringIO("abc\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_rotina_semanal()

def test_terminal_rejeita_data_inexistente(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-02-30\n"  # Data inexistente.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Não foi possível calcular:" in saida
    assert "Tempo restante:" not in saida
    assert "Tempo disponível no período:" not in saida

def test_terminal_rejeita_periodo_invertido(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-21\n"  # Data inicial
        "2026-10-19\n"  # Data final anterior à inicial.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"  # Domingo.
        "0\n"    # Quantidade de exceções: nenhuma.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Não foi possível calcular:" in saida
    assert "Tempo restante:" not in saida
    assert "Tempo disponível no período:" not in saida

def test_ler_excecoes_aceita_quantidade_zero(monkeypatch):
    entradas = StringIO("0\n")
    monkeypatch.setattr("sys.stdin", entradas)

    saida = ler_excecoes()

    assert saida == {}

def test_ler_excecoes_le_datas_e_minutos(monkeypatch):
    entradas = StringIO("2\n2026-10-22\n0\n2026-10-24\n30.5\n")
    monkeypatch.setattr("sys.stdin", entradas)

    saida = ler_excecoes()

    assert saida == {
        date(2026, 10, 22): 0,
        date(2026, 10, 24): 30.5,
    }

def test_ler_excecoes_rejeita_quantidade_negativa(monkeypatch):
    entradas = StringIO("-1\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError):
        ler_excecoes()

def test_ler_excecoes_rejeita_minutos_negativos(monkeypatch):
    entradas = StringIO("1\n2026-10-22\n-10\n")
    monkeypatch.setattr("sys.stdin", entradas)

    with pytest.raises(ValueError, match="Os minutos da exceção"):
        ler_excecoes()

def test_ler_excecoes_data_repetida_substitui_minutos(monkeypatch):
    entradas = StringIO("2\n2026-10-22\n60\n2026-10-22\n30\n")
    monkeypatch.setattr("sys.stdin", entradas)

    saida = ler_excecoes()

    assert saida == {date(2026, 10, 22): 30}

def test_terminal_aplica_excecao_zero_na_disponibilidade(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"         # Domingo.
        "1\n"           # Uma exceção.
        "2026-10-19\n"  # Data da exceção.
        "0\n"           # Zero minutos disponíveis nessa data.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Tempo restante: 23.0 minutos" in saida
    assert "Tempo disponível no período: 0.0 minutos" in saida
    assert "As atividades pendentes não cabem no tempo disponível." in saida

def test_terminal_rejeita_excecao_com_minutos_negativos(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.chdir(tmp_path)
    entradas = StringIO(
        "1\n"
        "Banco de Dados\nAula 1\n2\n"
        "Parte 1\n29\ns\n"
        "Parte 2\n26\nn\n"
        "10\n"          # Revisão pendente.
        "0\n"           # Apenas calcular.
        "2\n"           # Velocidade dos vídeos.
        "2026-10-19\n"  # Data inicial: segunda-feira.
        "2026-10-19\n"  # Data final: o mesmo dia.
        "30\n"          # Segunda-feira.
        "60\n"          # Terça-feira.
        "60\n"          # Quarta-feira.
        "60\n"          # Quinta-feira.
        "60\n"          # Sexta-feira.
        "120\n"         # Sábado.
        "120\n"         # Domingo.
        "1\n"           # Uma exceção.
        "2026-10-19\n"  # Data da exceção.
        "-10\n"         # Minutos negativos: entrada inválida.
    )
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "Não foi possível calcular: Os minutos da exceção não podem ser negativos." in saida
    assert "Tempo restante:" not in saida
    assert "Tempo disponível no período:" not in saida
