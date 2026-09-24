# Academic Hub

O Academic Hub é um projeto em desenvolvimento que tem como objetivo ajudar na organização da rotina acadêmica de forma flexível tornando o dia a dia do estudante mais organizado e previsível.

Atualmente, o projeto calcula o tempo de reprodução de vídeos conforme a velocidade escolhida. A função valida a duração e a velocidade, rejeitando valores iguais ou inferiores a zero. 

Calcula o tempo da aula total com a revisão considerando todas microaulas do mesmo tempo e velocidade. A função valida quantidade de microaulas e permite revisão de zero minutos.

Os testes automatizados verificam cálculos válidos e a rejeição dessas entradas inválidas.

## Como executar os testes

Com o Python instalado, execute no terminal, a partir da pasta do projeto:

```powershell
python test_calculos.py
```

Se todas as verificações passarem, será exibida a mensagem `Teste passou`.