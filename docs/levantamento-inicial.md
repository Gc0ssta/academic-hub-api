# Academic Hub — requisitos iniciais

Versão 0.5 · 24/09/2026

## 1. Problema e objetivo

Organizar aulas, revisões e avaliações exige acompanhar prazos, calcular a carga diária e reservar tempo para realizar os projetos. Quando o progresso muda, esse planejamento precisa ser recalculado.

O Academic Hub busca centralizar essas informações e distribuir as atividades pelo tempo disponível, indicando quando não for possível cumprir o planejamento. O problema e o cenário de uso abaixo foram validados; as propostas de funcionamento continuam em definição.

## 2. Cenário de referência

As informações abaixo descrevem a rotina levantada, não regras universais ou oficiais de uma instituição:

- Duas disciplinas compartilham a disponibilidade diária. Cada uma possui dois projetos e uma prova, com prazos correspondentes atualmente iguais entre as disciplinas.
- Cada projeto depende de determinadas aulas; para a prova, considera-se todo o conteúdo da disciplina. O objetivo é cumprir os prazos regulares.
- O padrão observado é de cinco microaulas de 30 minutos por aula completa. A reprodução costuma ocorrer em 2×, com possibilidade de outras velocidades.
- Cada aula completa tem uma revisão estimada em dez minutos, apoiada em resumos de dois PDFs referentes àquela aula.
- A disponibilidade para a faculdade é de 60 a 80 minutos por dia útil e de 120 a 180 minutos por dia no fim de semana. É separada do tempo de desenvolvimento deste projeto.
- Exercícios são desejáveis quando houver espaço. Imprevistos podem reduzir a disponibilidade ou deixar atividades pendentes.

## 3. Comportamentos esperados

- Registrar disciplinas, conteúdo, avaliações, prazos e disponibilidade diária.
- Calcular o tempo de vídeo conforme a velocidade escolhida e acrescentar a revisão uma vez por aula completa.
- Exigir duração original e velocidade maiores que zero no cálculo de tempo de vídeo. Valores iguais a zero ou negativos devem ser rejeitados com uma mensagem explicativa. A duração original é distinta do progresso: concluir um vídeo não altera sua duração para zero.
- Aceitar tempo de revisão maior ou igual a zero. Zero representa uma aula planejada sem tempo reservado para revisão; valores negativos devem ser rejeitados com `ValueError` e mensagem explicativa.
- Exigir quantidade de microaulas do tipo Python `int` e maior que zero. Outros tipos devem gerar `TypeError`; quantidades inteiras iguais a zero ou negativas devem gerar `ValueError`.
- Vincular cada microaula e revisão à sua aula e disciplina. Conteúdos de aulas diferentes não devem ser agrupados como uma única aula concluída.
- Respeitar a disponibilidade diária total, somando todas as disciplinas.
- Distinguir o prazo regular de entrega da meta de concluir as aulas, que deve considerar a reserva para realizar o projeto.
- Acompanhar o progresso e atualizar as atividades pendentes quando houver mudanças.
- Informar quando o tempo necessário não couber no período disponível.

Propostas a validar: configurar durações e disponibilidade; registrar vídeos e revisões separadamente; agendar a revisão após os vídeos, inclusive em outro dia; permitir velocidades por conteúdo sem aumentá-las automaticamente; encaixar exercícios após avaliar os compromissos do período.

## 4. Primeira entrega proposta

Começar por uma calculadora em Python que receba duração dos vídeos, velocidade, tempo de revisão e disponibilidade, devolvendo o tempo estimado e se ele cabe nessa disponibilidade. Planejamento automático por dia, API e armazenamento serão etapas posteriores.

**Regra de cálculo:** tempo de reprodução = duração original ÷ velocidade. Somar os tempos dos vídeos e acrescentar a revisão da aula uma vez.

A implementação atual de `calcular_tempo_aula` considera microaulas com a mesma duração original e a mesma velocidade de reprodução. Ela multiplica o tempo de uma microaula pela quantidade e acrescenta o tempo de revisão. Durações e velocidades diferentes dentro de uma mesma aula exigirão uma evolução dessa função.

Exemplo: cinco microaulas de 30 minutos em 2×, com revisão de dez minutos, totalizam **85 minutos**. Pausas e exercícios não estão incluídos nessa estimativa.

### Exemplos para verificar o comportamento

| Situação | Resultado esperado |
|---|---|
| Vídeo de 30 minutos em 2× | 15 minutos de reprodução |
| Duração igual a zero ou negativa, com velocidade válida | Rejeitar a entrada com `ValueError` e mensagem explicativa |
| Velocidade igual a zero ou negativa, com duração válida | Rejeitar a entrada com `ValueError` e mensagem explicativa |
| Aula completa do exemplo acima | 85 minutos, incluindo uma revisão |
| Mesma aula do exemplo, com tempo de revisão zero | 75 minutos, considerando somente os vídeos |
| Tempo de revisão negativo, com as demais entradas válidas | Rejeitar a entrada com `ValueError` e mensagem explicativa |
| Uma microaula de 30 minutos em 2× e revisão de dez minutos | 25 minutos |
| Quantidade inteira de microaulas igual a zero ou negativa, com as demais entradas válidas | Rejeitar a entrada com `ValueError` e mensagem explicativa |
| Quantidade de microaulas de tipo diferente de `int`, com as demais entradas válidas | Rejeitar a entrada com `TypeError` e mensagem explicativa |
| Três microaulas de uma aula de A e duas de uma aula de B | Nenhuma das duas aulas tem todos os vídeos concluídos |
| Atividades de 75 minutos em um dia com 60 disponíveis | Indicar que o plano excede a disponibilidade em 15 minutos |

### Simulação manual

Cenário fictício: uma aula pendente de A e uma de B, cinco microaulas de 30 minutos cada, reprodução em 2× e revisão de dez minutos por aula. Capacidade: 60 minutos por dia.

| Dia | Atividades, na ordem | Total |
|---|---|---:|
| 1 | A: microaulas 1 a 4 | 60 min |
| 2 | A: microaula 5 e revisão; B: microaulas 1 e 2 | 55 min |
| 3 | B: microaulas 3 a 5 e revisão | 55 min |

São 170 minutos em uma capacidade de 180 minutos. Cada revisão ocorre após os vídeos correspondentes, conforme a proposta de agendamento. O exemplo verifica duração e capacidade; não comprova cumprimento de prazos nem reserva para projetos, que ainda dependem de dados concretos.

## 5. Limites e decisões pendentes

Antes de automatizar o cronograma, definir datas e conteúdos de um caso real, esforço dos projetos, divisão da reserva entre disciplinas, prioridade entre entregas e possibilidade de dividir uma microaula entre dias.

Cálculos de notas dependem de confirmar pesos, critérios de aprovação e penalidades. O desconto de 20% mencionado no levantamento foi um exemplo, não uma regra validada.

Notas, faltas, interface visual e disponibilização online ficam para etapas futuras. Importação de PDFs, geração de resumos com IA e integração com a universidade não fazem parte da primeira entrega.
