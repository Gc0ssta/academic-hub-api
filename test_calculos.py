from calculos import calcular_tempo_video, calcular_tempo_aula

assert calcular_tempo_video(30,1.5) == 20

assert calcular_tempo_video(30,2.0) == 15

try:
    calcular_tempo_video(30, 0)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar velocidade zero.")

try:
    calcular_tempo_video(0,1.5)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar duração zero.")

try:
    calcular_tempo_video(30,-1)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar velocidade negativa.")

try:
    calcular_tempo_video(-30,1.5)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar duração negativa.")

assert calcular_tempo_aula(30, 5, 2, 10) == 85

assert calcular_tempo_aula(30, 5, 2, 0) == 75

assert calcular_tempo_aula(30, 1, 2, 10) == 25

try:
    calcular_tempo_aula(30, 5, 2, -10)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar tempo de revisão negativos")

try:
    calcular_tempo_aula(30, 2.5, 2, 10)
except TypeError:
    pass
else:
    raise AssertionError("A função deveria rejeitar valores que nao sao inteiros na quantidade de micro aulas")

try:
    calcular_tempo_aula(30, 0, 2, 10)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar zero na quantidade de micro aulas")

try:
    calcular_tempo_aula(30, -1, 2, 10)
except ValueError:
    pass
else:
    raise AssertionError("A função deveria rejeitar numeros negativos na quantidade de micro aulas")


print("Teste passou")