# Academic Hub

O Academic Hub é um projeto em desenvolvimento para acompanhar o progresso de aulas e revisões e estimar se as atividades pendentes cabem no tempo disponível. Atualmente, funciona pelo terminal, com armazenamento local em JSON.

## Funcionalidades

- Informar aulas e microaulas, com a duração individual e o estado de conclusão de cada vídeo.
- Selecionar uma aula e marcar uma de suas microaulas como concluída.
- Concluir a revisão de uma aula quando todas as suas microaulas estiverem concluídas.
- Informar os minutos disponíveis de segunda a domingo e aplicar essa rotina às datas do período escolhido, incluindo dias com zero minutos.
- Informar exceções de disponibilidade para datas específicas, sem alterar a rotina semanal.
- Calcular o tempo total pendente, considerando a velocidade dos vídeos e as revisões de cada aula.
- Comparar o tempo necessário com o tempo disponível, informando se as atividades cabem nesse período.
- Salvar as informações das aulas e microaulas em JSON e recuperá-las nas próximas execuções.

## Preparação

Projeto testado com Python 3.12.0. Os comandos abaixo são para
Windows com PowerShell, executados a partir da pasta do projeto.

Na primeira configuração, crie o ambiente virtual e instale as
dependências de desenvolvimento:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

## Como usar o Academic Hub

Após concluir a preparação, execute o programa na pasta do projeto:

```powershell
.\.venv\Scripts\python.exe main.py
```

No primeiro uso, sem aulas salvas, o programa solicita o cadastro das aulas e microaulas. Nas próximas execuções, recupera os dados do arquivo `aulas.json`.

Após cadastrar ou recuperar as aulas, escolha uma opção:

- `0`: apenas calcular o tempo pendente.
- `1`: marcar uma microaula como concluída.
- `2`: concluir a revisão de uma aula.

Para concluir uma revisão, todas as microaulas daquela aula precisam estar concluídas. Finalizar os vídeos não conclui a revisão automaticamente.

Em seguida, informe a velocidade dos vídeos, a data inicial, a data final e os minutos disponíveis em cada dia da semana, de segunda a domingo. Use datas no formato `AAAA-MM-DD` e ponto nos valores decimais, como `1.5` para a velocidade. Dias sem disponibilidade devem receber `0` minutos.

Após informar a rotina semanal, indique quantas exceções deseja cadastrar. Digite `0` se não houver nenhuma. Para cada exceção, informe a data e os minutos disponíveis, que substituirão os minutos previstos pela rotina naquela data. Zero minutos também é permitido. Se a mesma data for informada mais de uma vez, vale o último valor.

O período inclui a data inicial e a final. O programa aplica a rotina semanal e as exceções às datas desse intervalo e compara a soma dos minutos disponíveis com o tempo pendente das atividades. Exceções fora do período não afetam o total. Ainda não distribui atividades por dia nem verifica prazos de entrega.

Após um cálculo bem-sucedido, o cadastro e o progresso são salvos em `aulas.json`, na pasta de execução. O período, a rotina semanal e as exceções não são salvos e precisam ser informados novamente a cada execução.

Para registrar outra conclusão, execute o programa novamente. Ainda não é possível editar títulos e durações ou desfazer conclusões pelo terminal.

## Como executar os testes

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```
O relatório mostra o resultado de cada teste. Todos devem passar.