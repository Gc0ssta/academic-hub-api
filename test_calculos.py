from calculos import calcular_tempo_video

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

print("Teste passou")