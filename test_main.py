from io import StringIO

from main import main


def test_terminal_informa_que_atividades_cabem(monkeypatch, capsys):
    entradas = StringIO("5\n2\n30\n2\n10\n60\n")
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "faltam: 3 MicroAulas!" in saida
    assert "Tempo restante: 55.0 minutos" in saida
    assert "As atividades pendentes cabem no tempo disponível." in saida

def test_terminal_informa_que_atividades_nao_cabem(monkeypatch, capsys):
    entradas = StringIO("5\n2\n30\n2\n10\n40\n")
    monkeypatch.setattr("sys.stdin", entradas)

    main()

    saida = capsys.readouterr().out

    assert "faltam: 3 MicroAulas!" in saida
    assert "Tempo restante: 55.0 minutos" in saida
    assert "As atividades pendentes não cabem no tempo disponível." in saida

def test_terminal_informa_erro_microaulas_concluidas_maior_que_microaulas_totais(monkeypatch, capsys):
    entradas = StringIO("5\n6\n30\n2\n10\n60\n")
    monkeypatch.setattr("sys.stdin", entradas)

    main()
    
    saida = capsys.readouterr().out
    
    assert "Não foi possível calcular: A quantidade concluída não pode superar o total." in saida
    assert "Tempo restante: " not in saida