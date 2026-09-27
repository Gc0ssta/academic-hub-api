import pytest

from calculos import calcular_tempo_video, calcular_tempo_aula

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