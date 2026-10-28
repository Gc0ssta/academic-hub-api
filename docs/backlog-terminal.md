# Academic Hub — backlog da fase Terminal

Objetivo de produto confirmado; regras e tarefas em definição · 27/10/2026

Este documento organiza trabalho restante, sem aprovar automaticamente regras de produto. A ordem é uma sugestão baseada nas dependências técnicas. Os identificadores T01–T12 são locais; não correspondem a issues publicadas no GitHub. Uma issue pode precisar de mais de um commit coerente.

## Objetivo para encerrar a fase

Usar o terminal para cadastrar conteúdos e entregas, configurar disponibilidade, consultar atividades planejadas por data e recalcular as pendências após mudanças de progresso ou disponibilidade. O planejamento deve respeitar o tempo compartilhado entre disciplinas, as dependências e os prazos definidos, mostrando o que não couber.

O objetivo foi confirmado: um planejador utilizável pelo terminal, com visão geral do período e detalhamento das atividades de cada dia, incluindo estudo, revisões, execução de projetos e provas. As regras de distribuição, reservas e interação continuam pendentes; confirmar o objetivo não aprova automaticamente cada solução proposta abaixo.

## Como reconhecer a entrega pronta

A fase deve permitir percorrer este fluxo sem editar manualmente arquivos de dados:

1. Cadastrar e corrigir disciplinas/conteúdos, progresso, entregas, prazos regulares e as estimativas necessárias para o planejamento.
2. Configurar e reutilizar a rotina semanal, a velocidade escolhida e exceções de disponibilidade por data.
3. Consultar uma visão geral do período, com prazos e tempo reservado para preparar projetos e provas, e consultar o detalhe de cada dia com atividades identificáveis e minutos estimados.
4. Registrar o que realmente foi feito. Se cinco atividades estavam planejadas e apenas três foram concluídas, as outras duas continuam pendentes.
5. Recalcular as pendências futuras conforme as regras aprovadas, mostrando a nova distribuição e os impactos sobre as entregas. Não ultrapassar a capacidade, duplicar tempo ou alterar a velocidade silenciosamente.
6. Fechar e abrir o programa, recuperar cadastro, progresso e configurações e gerar novamente o plano a partir deles.

O sistema estima com os dados informados; não garante cumprimento de prazos quando falta capacidade ou as estimativas não correspondem à execução. A entrega deve explicar quais atividades ou entregas ficam comprometidas, em vez de apresentar um plano impossível como viável.

### Limite confirmado para esta entrega

Decisão confirmada em 27/10/2026: a fase termina com um plano diário consultável e recalculável, conforme regras explícitas, que o usuário pode ajustar ao alterar suas informações. A sugestão e comparação automática de vários planos (por exemplo, dividir o atraso em dois dias ou simular outra velocidade) ficam para depois desta fase. Mudanças de velocidade ou de disponibilidade dependem de escolha do usuário.

Uma tabela textual pode atender às visões de período e de dia. Um calendário gráfico ou uma interface de terminal elaborada não é requisito por si só; validar se a informação fica clara e utilizável.

## O que já existe

- Cadastro inicial de aulas e microaulas, duração individual e progresso.
- Conclusão de microaulas e de revisões; revisão só pode ser concluída após os vídeos.
- Persistência de aulas e progresso em JSON.
- Cálculo do tempo pendente com uma velocidade comum aos vídeos e revisão separada.
- Leitura de datas, rotina semanal e exceções pelo terminal.
- Disponibilidade por data: exceções substituem a rotina; zero é permitido; data repetida usa o último valor.
- Comparação entre o total pendente e o total disponível no período.
- Testes automatizados e execução no GitHub Actions.

Reexecutar o programa com outros dados já recalcula os totais. Isso ainda não produz um cronograma de atividades nem verifica prazos por entrega. Exceções fora do período não afetam a soma, e passar um dia não marca nenhuma atividade como concluída.

## Decisões de produto pendentes

Antes de T04 e T05:

- Uma microaula pode ser dividida entre dias? Se puder, como registrar progresso parcial e minutos restantes?
- Qual ordem seguir entre disciplinas e entre microaulas? Como resolver empates?
- A revisão precisa ocorrer depois de todos os vídeos também no agendamento? Pode ser dividida?
- Qual é a data de referência do recálculo? Se for hoje, a disponibilidade informada representa o dia inteiro ou apenas o tempo restante?
- Como tratar pendências de dias passados? Não presumir que foram concluídas.

Antes de T09–T11:

- Qual convenção de prazo usar: data inclusiva, horário limite ou outra regra?
- A margem para um projeto é expressa em dias de calendário, dias de estudo, minutos de execução ou uma combinação? Como se distribui entre disciplinas?
- Como conciliar a reserva diária para exercícios com a disponibilidade e as entregas? O que fazer se a reserva superar os minutos disponíveis?
- Quais atividades devem preceder cada entrega e como priorizar prazos concorrentes?

Antes de T08:

- Se uma microaula concluída for reaberta depois da revisão, o que deve acontecer com a revisão? Hoje o sistema guarda apenas os minutos pendentes, sem conservar uma duração original separada.

## Issues propostas

### T01 — Preservar progresso antes das perguntas do cálculo

**Estado:** concluída e validada localmente em 27/10/2026. A gravação ocorre uma única vez, após a ação válida e antes das perguntas do cálculo. Testes cobrem cadastro, conclusão de microaula e conclusão de revisão preservados após data inválida. README atualizado; suíte com 113 testes passando. Commit e CI ainda a conferir.

**Problema:** marcar uma conclusão e depois informar uma data inválida perde a alteração, porque a gravação só acontece após o cálculo.

**Aceite:**
- Salvar após a opção válida e a ação terminarem sem erro, antes de pedir os dados do cálculo.
- Confirmar, relendo o arquivo, que a conclusão permanece após um erro de data.
- Preservar a rejeição de revisão com vídeos pendentes e informar falhas de gravação sem afirmar sucesso.
- Atualizar o README para o novo momento da gravação.

**Dependências:** nenhuma.

### T02 — Definir o comportamento do planejador com um exemplo manual

**Estado:** decisão de produto; necessária antes do algoritmo.

**Aceite:**
- Resolver as decisões de divisão, ordem, revisão e data de referência listadas acima.
- Montar um exemplo pequeno de duas disciplinas compartilhando os mesmos minutos diários, com resultado esperado por data.
- Incluir um dia com zero, uma atividade concluída e uma situação que não cabe; calcular o resultado esperado sem usar o algoritmo a ser desenvolvido.
- Confirmar o que encerra a fase Terminal e quais reservas entram nela.

**Dependências:** nenhuma. Não exige uma funcionalidade nova.

### T03 — Representar atividades pendentes para o agendamento

**Problema:** o total de minutos não informa qual vídeo ou revisão deve ser realizado em cada data.

**Aceite:**
- Produzir atividades identificáveis, vinculadas à aula e à disciplina, com duração restante e dependências conforme T02.
- Excluir atividades concluídas e incluir revisão pendente uma única vez.
- Manter o cadastro e as regras de cálculo existentes; definir referências que continuem válidas quando o cadastro for editado.
- Se T02 permitir divisão, representar os minutos restantes sem confundir duração original com progresso.

**Dependências:** T02.

### T04 — Distribuir atividades pela disponibilidade de cada data

**Aceite:**
- Consumir as disponibilidades que já são geradas pela rotina e pelas exceções.
- Respeitar ordem, dependências e divisão definidas em T02.
- Somar todas as disciplinas no mesmo limite diário; nunca reservar o mesmo minuto duas vezes.
- Retornar atividades por data, minutos utilizados e atividades que não couberam. Não alterar o progresso ao planejar.
- Reproduzir o exemplo manual de T02. Nesta primeira versão, não afirmar que prazos de entregas foram cumpridos.

**Dependências:** T03.

### T05 — Recalcular atividades futuras após mudanças

**Aceite:**
- Regerar a distribuição a partir do progresso atual, da disponibilidade atual e da data de referência definida em T02.
- Uma exceção de zero retirar a capacidade apenas da data correspondente; redistribuir o trabalho restante conforme a regra aprovada.
- Não marcar tarefas como feitas pela passagem do tempo, não contar dias passados como capacidade futura e não aumentar a velocidade automaticamente.
- Mesmas entradas produzirem o mesmo resultado; se não houver espaço, informar as pendências que ficaram de fora.

**Dependências:** T04 e decisões de T02. Não exige criar um serviço em segundo plano nem guardar versões anteriores do cronograma.

### T06 — Consultar e recalcular o cronograma pelo terminal

**Aceite:**
- Oferecer uma ação para consultar o plano com data, disciplina, aula, atividade, minutos utilizados e limite do dia.
- Permitir consultar o resumo do período e o detalhe de uma data, incluindo reservas e prazos quando T09–T11 estiverem implementadas.
- Permitir recalcular após registrar progresso ou modificar a disponibilidade, reaproveitando T05.
- Diferenciar atividade planejada de atividade concluída e mostrar as pendências sem espaço.
- Explicar o impacto do recálculo: o que permanece pendente, sua nova distribuição e eventuais entregas comprometidas.
- Mostrar a data de referência e informar quando não houver pendências.

**Dependências:** T05. Reaproveitar o menu e as funções de entrada existentes.

### T07 — Persistir as configurações de planejamento em JSON

**Problema:** período, rotina e exceções precisam ser digitados em toda execução.

**Aceite:**
- Salvar e carregar período, rotina e exceções, com uma representação explícita das datas e das chaves da semana no JSON.
- Permitir reutilizar ou alterar as configurações; confirmar se a velocidade comum também deve ser persistida.
- Continuar carregando os arquivos de aulas existentes sem perda de progresso.
- Tratar arquivo ausente e inválido separadamente; não sobrescrever dados inválidos silenciosamente e comunicar erro de gravação.
- Configurações antigas não devem fazer um recálculo consumir disponibilidade de dias passados.

**Dependências:** decisões de data de referência de T02; pode ser feita antes de T04. A escolha dos arquivos e a conversão das datas são decisões técnicas a explicar antes da implementação.

### T08 — Acrescentar e corrigir dados após o primeiro cadastro

**Problema:** com aulas já salvas, o terminal atualmente não oferece novo cadastro nem correção do conteúdo existente.

**Aceite:**
- Adicionar aulas a um conjunto já salvo e corrigir título ou duração de uma microaula.
- Permitir corrigir uma conclusão registrada por engano, conforme a decisão sobre revisão e reabertura.
- Preservar os dados não editados e salvar uma alteração válida independentemente de um cálculo posterior.
- Fazer o próximo recálculo usar os dados corrigidos.

**Dependências:** T01 e decisão de reabertura. Ajustar as referências de T03 se necessário. Exclusão em massa não faz parte desta issue.

### T09 — Cadastrar entregas e seus conteúdos necessários

**Aceite:**
- Registrar projeto ou prova, disciplina, prazo regular e aulas necessárias, com a convenção de prazo aprovada.
- Permitir consultar e corrigir essas informações pelo terminal e recuperá-las em outra execução.
- Uma aula usada por mais de uma entrega deve continuar sendo o mesmo conteúdo, sem duplicar seu tempo.
- Confirmar quais revisões e atividades de execução pertencem a cada entrega.

**Dependências:** T02, T03 e T08. Não calcular notas nem penalidades nesta issue.

### T10 — Representar as reservas de execução, revisão e exercícios

**Estado:** escopo a confirmar; implementar somente as reservas escolhidas para esta fase.

**Aceite:**
- Representar a margem entre terminar conteúdos e entregar o projeto, distinguindo margem de calendário de esforço em minutos.
- Se incluída, descontar a reserva de exercícios da capacidade diária: 80 minutos totais com 20 reservados deixam 60 para outras atividades.
- Conciliar reservas de duas disciplinas sem duplicar capacidade e explicitar quando uma reserva for inviável.
- Evitar contar novamente a revisão da aula como outra atividade idêntica.

**Dependências:** T02 e T09; unidades e prioridades precisam estar decididas antes do código.

### T11 — Considerar prazos e reservas na distribuição e no recálculo

**Aceite:**
- Evoluir T04 e T05 para respeitar os prazos, dependências e reservas aprovados.
- Compartilhar a capacidade diária entre entregas e disciplinas, usando o critério de prioridade definido.
- Demonstrar um caso em que o total do período é suficiente, mas uma entrega antecipada não pode ser cumprida.
- Exibir a entrega comprometida e o trabalho restante sem ocultar excesso nem trocar automaticamente o prazo regular por um prazo com penalidade.
- Recalcular após uma exceção ou atualização de progresso mantendo essas mesmas regras.

**Dependências:** T09, T10 e T05. Os testes devem usar resultados esperados definidos a partir das regras, não copiados do algoritmo.

### T12 — Validar o uso completo e encerrar a fase Terminal

**Aceite:**
- Executar um cenário representativo com duas disciplinas, conteúdos, entregas, rotina e exceções.
- Fechar e abrir o programa, registrar progresso, corrigir um dado e simular um dia perdido; conferir persistência e novo plano.
- Verificar períodos viáveis, inviáveis, dias com zero e todas as atividades concluídas.
- Atualizar README, exemplos e estado dos requisitos; distinguir o levantamento histórico das funcionalidades implementadas.
- Conferir mensagens e testes relevantes, executar a suíte e verificar o CI.

**Dependências:** issues incluídas no escopo final. Não depende de atingir uma quantidade de testes ou um número de commits.

## Ordem sugerida e limites

T01 está concluída localmente. Para o foco no recalculador, a sequência técnica é T02 → T03 → T04 → T05 → T06. T07 e T08 tornam o uso recorrente mais prático e podem ser priorizadas antes. T09 → T10 → T11 completam o planejamento por entregas. T12 verifica o conjunto aprovado.

API, interface web, autenticação, PostgreSQL, Docker, nuvem, importação de PDFs e integração com o portal não são planejados neste backlog. Notas, faltas e regras de penalidade também ficam fora da proposta desta fase, conforme os limites já registrados; sua inclusão exigiria uma decisão explícita de escopo.

Reorganizar pastas ou aplicar padrões de projeto não é condição automática para concluir uma issue. Fazer refatorações quando ajudarem uma mudança concreta, sem reconstruir o que já funciona.
