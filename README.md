# Academic Hub

O Academic Hub é um projeto em desenvolvimento que tem como objetivo ajudar na organização da rotina acadêmica de forma flexível tornando o dia a dia do estudante mais organizado e previsível.

## Funcionalidades

- Informar aulas e microaulas, com a duração individual e o estado de conclusão de cada vídeo.
- Calcular o tempo total pendente, considerando a velocidade dos vídeos e as revisões de cada aula.
- Comparar o tempo necessário com o tempo disponível, informando se as atividades cabem nesse período.
- Salvar as informações das aulas e microaulas em JSON e recuperá-las nas próximas execuções.

## Como usar o Academic Hub

O Academic Hub funciona pelo terminal. Execute os comandos na pasta do projeto, onde o programa procura e salva o arquivo `aulas.json`.

No primeiro uso, sem aulas salvas, o programa solicita o cadastro. Após um cálculo bem-sucedido, salva as informações em `aulas.json`.

Nas próximas execuções, recupera as aulas salvas e pergunta apenas a velocidade dos vídeos e o tempo disponível.

Ainda não é possível editar o cadastro ou marcar novas conclusões pelo terminal.

Antes de executar pela primeira vez, crie o ambiente virtual conforme as instruções abaixo. Use ponto nos valores decimais, como `1.5` para a velocidade.

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
.\.venv\Scripts\python.exe -m pytest -v
```
O relatório mostra o resultado de cada teste. Todos devem passar.