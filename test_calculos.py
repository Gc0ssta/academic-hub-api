import pytest

from calculos import calcular_tempo_video, calcular_tempo_aula, cabe_no_tempo, calcular_microaulas_pendentes

def test_calcular_tempo_video_em_velocidade_1_5():
    assert calcular_tempo_video(30, 1.5) == 20

def test_calcular_tempo_video_em_velocidade_2_0():
    assert calcular_tempo_video(30,2.0) == 15

def test_calcular_tempo_video_rejeita_velocidade_zero():
    with pytest.raises(ValueError):
        calcular_tempo_video(30, 0)

def test_calcular_tempo_video_rejeita_tempo_video_zero():
    with pytest.raises(ValueError):
        calcular_tempo_video(0,1.5)

def test_calcular_tempo_video_rejeita_velocidade_negativa():
    with pytest.raises(ValueError):
        calcular_tempo_video(30,-1)

def test_calcular_tempo_video_rejeita_duracao_negativa():
    with pytest.raises(ValueError):
        calcular_tempo_video(-30,1.5)

def test_calcular_tempo_aula_com_revisao_em_10():
    assert calcular_tempo_aula(
        duracao_microaula=30,
        quantidade_microaulas=5,
        velocidade=2,
        tempo_revisao=10,
    ) == 85

def test_calcular_tempo_aula_com_revisao_em_0():
    assert calcular_tempo_aula(
        duracao_microaula=30,
        quantidade_microaulas=5,
        velocidade=2,
        tempo_revisao=0,
    ) == 75
    
def test_calcular_tempo_aula_com_microaula_1():
    assert calcular_tempo_aula(
        duracao_microaula=30,
        quantidade_microaulas=1,
        velocidade=2,
        tempo_revisao=10,
    ) == 25

def test_calcular_tempo_aula_rejeita_revisao_negativa():
    with pytest.raises(ValueError):
        calcular_tempo_aula(30, 5, 2, -10)

def test_calcular_tempo_aula_rejeita_microaula_decimal():
    with pytest.raises(TypeError):
        calcular_tempo_aula(30, 2.5, 2, 10)

def test_calcular_tempo_aula_rejeita_microaula_zero():
    with pytest.raises(ValueError):
        calcular_tempo_aula(30, 0, 2, 10)

def test_calcular_tempo_aula_rejeita_microaula_negativa():
    with pytest.raises(ValueError):
        calcular_tempo_aula(30, -1, 2, 10)

def test_nao_cabe_quando_tempo_insuficiente():
    assert cabe_no_tempo(85, 60) is False

def test_cabe_no_tempo_quando_tempo_igual():
    assert cabe_no_tempo(85, 85) is True

def test_cabe_no_tempo_quando_tempo_disponivel_maior():
    assert cabe_no_tempo(85, 90) is True

def test_nao_cabe_no_tempo_quando_tempo_disponivel_0_e_menor_tempo_necessario():
    assert cabe_no_tempo(85, 0) is False

def test_cabe_no_tempo_quando_tempo_necessario_0_e_menor_tempo_disponivel():
    assert cabe_no_tempo(0, 60) is True

def test_cabe_no_tempo_quando_ambos_tempos_0():
    assert cabe_no_tempo(0, 0) is True

def test_cabe_no_tempo_rejeita_tempo_necessario_negativo():
    with pytest.raises(ValueError): 
        cabe_no_tempo(-1, 60)

def test_cabe_no_tempo_rejeita_tempo_disponivel_negativo():
    with pytest.raises(ValueError): 
        cabe_no_tempo(85, -1)

def test_aula_nao_cabe_em_sessenta_minutos():
    tempo_aula = calcular_tempo_aula(30, 5, 2, 10)
    assert cabe_no_tempo(tempo_aula, 60) is False

def test_duas_disciplinas_nao_cabem_em_120_minutos():
    tempo_atividades = [calcular_tempo_aula(30, 5, 2, 10), calcular_tempo_aula(30, 3, 2, 10)]
    tempo_total = sum(tempo_atividades)
    assert cabe_no_tempo(tempo_total, 120) is False

def test_calcular_microaulas_pendentes_total_5_concluidas_2():
    assert calcular_microaulas_pendentes(5, 2) == 3

def test_calcular_microaulas_pendentes_concluidas_0():
    assert calcular_microaulas_pendentes(5, 0) == 5

def test_calcular_microaulas_sem_pendencias():
    assert calcular_microaulas_pendentes(5, 5) == 0

def test_calcular_microaulas_pendentes_total_nao_pode_decimal():
    with pytest.raises(TypeError): 
        calcular_microaulas_pendentes(5.5, 2)

def test_calcular_microaulas_pendentes_concluidas_nao_pode_decimal():
    with pytest.raises(TypeError): 
        calcular_microaulas_pendentes(5, 2.5)

def test_calcular_microaulas_pendentes_total_nao_pode_ser_0():
    with pytest.raises(ValueError): 
        calcular_microaulas_pendentes(0, 0)

def test_calcular_microaulas_pendentes_total_nao_pode_ser_negativo():
    with pytest.raises(ValueError): 
        calcular_microaulas_pendentes(-5, 0)

def test_calcular_microaulas_pendentes_concluidas_nao_pode_ser_negativo():
    with pytest.raises(ValueError): 
        calcular_microaulas_pendentes(5, -1)

def test_calcular_microaulas_pendentes_concluidas_nao_pode_ser_maior_que_total():
    with pytest.raises(ValueError): 
        calcular_microaulas_pendentes(5, 6)