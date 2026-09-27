# Academic Hub

O Academic Hub é um projeto em desenvolvimento que tem como objetivo ajudar na organização da rotina acadêmica de forma flexível tornando o dia a dia do estudante mais organizado e previsível.

Atualmente, o projeto calcula o tempo de reprodução de vídeos conforme a velocidade escolhida. A função valida a duração e a velocidade, rejeitando valores iguais ou inferiores a zero. 

Calcula o tempo da aula total com a revisão considerando todas microaulas do mesmo tempo e velocidade. A função valida quantidade de microaulas e permite revisão de zero minutos.

Verifica se o tempo necessário para uma atividade cabe no tempo disponível. A função aceita tempos iguais a zero e rejeita valores negativos, retornando verdadeiro quando há tempo suficiente e falso quando não há.

Os testes automatizados verificam cálculos válidos e a rejeição dessas entradas inválidas.

## Como executar os testes

Projeto testado com Python 3.12.0. Os comandos abaixo são para
Windows com PowerShell, executados a partir da pasta do projeto.

Na primeira configuração, crie o ambiente virtual e instale as
dependências de desenvolvimento:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Para executar os testes:

```powershell
.\.venv\Scripts\python.exe -m pytest test_calculos.py -v
```
O relatório mostra o resultado de cada teste. Todos devem passar.