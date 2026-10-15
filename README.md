# Academic Hub

O Academic Hub é um projeto em desenvolvimento para acompanhar o progresso de aulas e revisões e estimar se as atividades pendentes cabem no tempo disponível. Atualmente, funciona pelo terminal, com armazenamento local em JSON.

## Funcionalidades

- Informar aulas e microaulas, com a duração individual e o estado de conclusão de cada vídeo.
- Selecionar uma aula e marcar uma de suas microaulas como concluída.
- Concluir a revisão de uma aula quando todas as suas microaulas estiverem concluídas.
- Informar a disponibilidade em minutos para cada dia de um período, incluindo dias com zero minutos disponíveis.
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

O Academic Hub funciona pelo terminal. Execute os comandos na pasta do projeto, onde o programa procura e salva o arquivo `aulas.json`.

No primeiro uso, sem aulas salvas, o programa solicita o cadastro. Após um cálculo bem-sucedido, salva as informações em `aulas.json`.

Após cadastrar ou recuperar as aulas, o programa apresenta três opções: `0` para apenas calcular o tempo pendente, `1` para concluir uma microaula e `2` para concluir uma revisão. Quando a opção é aceita, solicita a velocidade, quantidade de dias e minutos disponíveis em cada dia. Após um cálculo bem-sucedido, salva o cadastro e o progresso em `aulas.json`.

O programa compara o tempo pendente das atividades com a soma das disponibilidades. Ainda não distribui atividades por dia nem verifica prazos.

As disponibilidades são informadas novamente a cada execução; o JSON continua salvando apenas as aulas e o progresso.

Para registrar outra conclusão, execute o programa novamente.

Concluir todas as microaulas de uma aula não conclui a revisão automaticamente. A pessoa precisa selecionar essa ação.

Ainda não é possível editar títulos e durações ou desfazer conclusões pelo terminal.

Após concluir a preparação, execute o comando abaixo. Use ponto nos valores decimais, como `1.5` para a velocidade.

```powershell
.\.venv\Scripts\python.exe main.py
```

## Como executar os testes

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```
O relatório mostra o resultado de cada teste. Todos devem passar.