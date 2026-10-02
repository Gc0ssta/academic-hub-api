# Academic Hub

O Academic Hub é um projeto em desenvolvimento que tem como objetivo ajudar na organização da rotina acadêmica de forma flexível tornando o dia a dia do estudante mais organizado e previsível.

Atualmente, o projeto calcula o tempo de reprodução de vídeos conforme a velocidade escolhida. A função valida a duração e a velocidade, rejeitando valores iguais ou inferiores a zero. 

Calcula o tempo da aula total com a revisão considerando todas microaulas do mesmo tempo e velocidade. A função valida quantidade de microaulas e permite revisão de zero minutos.

Verifica se o tempo necessário para uma atividade cabe no tempo disponível. A função aceita tempos iguais a zero e rejeita valores negativos, retornando verdadeiro quando há tempo suficiente e falso quando não há.

Calcula quantas microaulas estão pendentes a partir do total e da quantidade concluída informados. Aceita zero pendências e rejeita quantidades inválidas.

Calcula o tempo restante da aula considerando as microaulas concluídas e o tempo de revisão pendente. Retorna apenas o tempo da revisão quando todos os vídeos foram concluídos, ou zero quando não há vídeos nem revisão pendentes. Rejeita tempo de revisão negativo.

Os testes automatizados verificam cálculos válidos e a rejeição dessas entradas inválidas.

## Como usar o Academic Hub

Atualmente, o Academic Hub funciona pelo terminal. O programa solicita informações sobre a aula e mostra quantas microaulas estão pendentes e o tempo restante, incluindo a revisão pendente. Também solicita o tempo disponpível para realizar as atividades e diz se cabe ou não cabe no tempo das atividades pendentes.

Antes de executar pela primeira vez, crie o ambiente virtual conforme as instruções abaixo. Use ponto nos valores decimais, como 1.5 para a velocidade.

```powershell
.\.venv\Scripts\python.exe main.py
```

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