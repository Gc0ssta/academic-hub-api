# Academic Hub — backlog da fase Terminal

Escopo do MVP Terminal e regras da T02 aprovados · atualizado em 02/11/2026

Este documento organiza trabalho restante, sem aprovar automaticamente regras de produto. A ordem é uma sugestão baseada nas dependências técnicas. Os identificadores T01–T12 são locais; não correspondem a issues publicadas no GitHub. Uma issue pode precisar de mais de um commit coerente.

## Objetivo para encerrar a fase

Usar o terminal para cadastrar conteúdos e entregas, configurar disponibilidade, consultar atividades planejadas por data e recalcular as pendências após mudanças de progresso ou disponibilidade. O planejamento deve respeitar o tempo compartilhado entre disciplinas, as dependências e os prazos definidos, mostrando o que não couber.

O objetivo foi confirmado: um planejador utilizável pelo terminal, com visão geral do período e detalhamento diário de estudo, revisões e execução de projetos. Provas são apresentadas por janela de realização e estado, sem agendamento de duração. As regras, os exemplos e a visão global do MVP foram aprovados em 02/11/2026, encerrando a T02. A aprovação do escopo não significa que o planejador já esteja implementado; os detalhes técnicos serão resolvidos nas tarefas seguintes.

## Como reconhecer a entrega pronta

A fase deve permitir percorrer este fluxo sem editar manualmente arquivos de dados:

1. Cadastrar e corrigir disciplinas/conteúdos, progresso, entregas, prazos regulares e as estimativas necessárias para o planejamento.
2. Configurar e reutilizar a rotina semanal, a velocidade escolhida e exceções de disponibilidade por data.
3. Consultar uma visão geral do período, com prazos, estudo e tempo reservado para executar projetos, e consultar o detalhe diário dessas atividades com minutos estimados. Para provas, consultar a janela, as pendências de preparação e o estado de liberação/conclusão, sem reserva de minutos para realizá-las.
4. Registrar o que realmente foi feito. Se cinco atividades estavam planejadas e apenas três foram concluídas, as outras duas continuam pendentes.
5. Recalcular as pendências futuras conforme as regras aprovadas, mostrando a nova distribuição e os impactos sobre as entregas. Não ultrapassar a capacidade, duplicar tempo ou alterar a velocidade silenciosamente.
6. Fechar e abrir o programa, recuperar cadastro, progresso e configurações e gerar novamente o plano a partir deles.

O sistema estima com os dados informados; não garante cumprimento de prazos quando falta capacidade ou as estimativas não correspondem à execução. A entrega deve explicar quais atividades ou entregas ficam comprometidas, em vez de apresentar um plano impossível como viável.

### Limite confirmado para esta entrega

Decisão confirmada em 27/10/2026: a fase termina com um plano diário consultável e recalculável, conforme regras explícitas, que o usuário pode ajustar ao alterar suas informações. A sugestão e comparação automática de vários planos (por exemplo, dividir o atraso em dois dias ou simular outra velocidade) ficam para depois desta fase. Mudanças de velocidade ou de disponibilidade dependem de escolha do usuário.

Confirmado em 29/10/2026: considerar somente prazos regulares nesta fase, sem prazos extras, penalidades ou recomendações automáticas de ajustes. Quando o plano não couber, identificar as entregas comprometidas e permitir ajustes manuais de disponibilidade, velocidade e estimativa de um projeto específico, seguidos de recálculo. Permitir voltar ou sair preservando os dados, sem exigir uma solução viável para encerrar a operação.

Uma tabela textual pode atender às visões de período e de dia. Um calendário gráfico ou uma interface de terminal elaborada não é requisito por si só; validar se a informação fica clara e utilizável.

Decisão de 02/11/2026: a reserva diária de exercícios fica fora da fase Terminal. O usuário pode fazer exercícios por conta própria; o programa não os agenda, desconta da disponibilidade nem exige registro de conclusão. Uma inclusão futura permanece opcional, sem compromisso de implementação.

## O que já existe

- Cadastro inicial de aulas e microaulas, duração individual e progresso.
- Conclusão de microaulas e de revisões; revisão só pode ser concluída após os vídeos.
- Persistência de aulas e progresso em JSON.
- Cálculo do tempo pendente com uma velocidade comum aos vídeos e revisão separada.
- Leitura de datas, rotina semanal e exceções pelo terminal.
- Disponibilidade por data: exceções substituem a rotina; zero é permitido; data repetida usa o último valor.
- Comparação entre o total pendente e o total disponível no período.
- Função auxiliar que transforma microaulas pendentes em atividades com tipo, título e tempo estimado, preservando a ordem e os dados originais. Ainda sem integração ao terminal ou distribuição por datas.
- Testes automatizados e execução no GitHub Actions.

Reexecutar o programa com outros dados já recalcula os totais. Isso ainda não produz um cronograma de atividades nem verifica prazos por entrega. Exceções fora do período não afetam a soma, e passar um dia não marca nenhuma atividade como concluída.

## Regras de planejamento confirmadas — atualizadas em 02/11/2026

- Microaulas serão planejadas inteiras em uma data, usando a duração estimada na velocidade escolhida. Não dividir automaticamente o mesmo vídeo entre dias nesta fase.
- A disponibilidade representa o total de minutos para estudar no dia, não exige um bloco contínuo de horário. Pausas e retomadas no mesmo dia são compatíveis com essa regra.
- O progresso de uma microaula continua sendo concluída ou pendente. O sistema não mede tempo efetivamente estudado nem registra posição parcial do vídeo.
- Uma microaula de 20 minutos não pode ser atribuída a um dia com apenas 15 minutos de capacidade ainda não alocada. Essa sobra pode existir no plano sem ser uma falha.
- O usuário pode aumentar explicitamente a disponibilidade de uma data por uma exceção e solicitar recálculo. O sistema pode antecipar atividades que passem a caber, respeitando a sequência e as dependências aprovadas; não garantir a antecipação de uma atividade específica.
- Não aumentar automaticamente disponibilidade ou velocidade. Uma atividade que não cabe em nenhuma data elegível deve ser apresentada como pendência sem espaço.

Capacidade ainda não alocada no plano não é medição de tempo livre real durante o dia.

### Prazo regular inclusivo

- O dia informado como prazo regular integra o período disponível para planejamento. Para projetos, a entrega pode ocorrer até 23h59 dessa data, no horário de Brasília, conforme a regra de produto confirmada em 29/10/2026.
- Exemplo: com prazo no dia 24, é permitido planejar trabalho no próprio dia 24, respeitando sua disponibilidade. No dia 25, um projeto ainda pendente está com o prazo regular encerrado.
- Usar a data no horário de Brasília como referência para identificar a passagem do prazo. O planejamento desta fase distribui minutos por dia, sem agendar horários específicos dentro dele; incluir a data final não mede quantos minutos ainda restam até o horário limite.

### Pendências de dias passados

- Ao recalcular, usar o progresso registrado: retirar da distribuição as atividades concluídas e manter as não concluídas na sequência obrigatória, mesmo que estivessem previstas para um dia passado. Decisão confirmada em 29/10/2026.
- Redistribuir as pendências pela capacidade disponível de hoje em diante, sem transferir minutos não utilizados de dias passados. A passagem do tempo não conclui atividades.
- O usuário não precisa cadastrar uma exceção de zero por não ter realizado todas as atividades previstas. Basta registrar o que concluiu; as demais permanecem pendentes e são redistribuídas ao atualizar o plano em uma nova data. Decisão de 02/11/2026.
- Na fase Terminal, verificar a data atual de Brasília ao abrir o programa e antes de consultar ou recalcular o plano. Se o dia mudou, atualizar a distribuição a partir dessa data. Não depender de um processo executando à meia-noite: com o programa fechado, a atualização ocorre na próxima abertura; com ele aberto, na próxima consulta ou recálculo.
- Recalcular também as atividades seguintes, respeitando dependências e prazos. Informar trabalho sem espaço e entregas comprometidas, sem aumentar disponibilidade ou mudar prazos automaticamente.

### Conclusão e capacidade do dia atual

- Os minutos são estimativas para planejamento, não uma medição do tempo efetivamente estudado. O sistema considera a conclusão registrada pelo usuário, sem cronometrar sua execução.
- Se o usuário reduzir a disponibilidade de hoje para zero depois de registrar uma conclusão, aceitar a alteração, preservar a conclusão e redistribuir as atividades pendentes. Mostrar separadamente o que já foi concluído e o que ainda está planejado; não gerar capacidade restante negativa nem desfazer progresso para adequá-lo à nova disponibilidade. Esse ajuste é opcional, não requisito para tratar atrasos.
- Aplicar a sequência também ao registro de conclusão das atividades de estudo: uma microaula posterior ou revisão não pode ser concluída pulando a próxima atividade pendente. A antecipação traz somente a próxima atividade elegível para hoje e não a conclui automaticamente. Preservar as escolhas já aprovadas dentro de blocos conjuntos de projetos e entre provas liberadas, sem impor uma ordem adicional entre elas.
- Concluir uma atividade de hoje não libera seu espaço planejado para preencher automaticamente com outra atividade. As demais atividades de hoje permanecem previstas; a conclusão, por si só, não aumenta a carga do dia. Decisão confirmada em 29/10/2026.
- Exemplo: com três microaulas de 20 minutos planejadas em um dia de 60 minutos, concluir a primeira mantém as outras duas para hoje, sem acrescentar uma quarta microaula.
- Para trazer uma atividade futura para hoje, o usuário usa a antecipação explícita descrita abaixo. Não reutilizar automaticamente a capacidade das atividades concluídas, inclusive após fechar e abrir o programa ou repetir um recálculo.
- A representação e persistência das alocações do dia e das antecipações serão definidas na implementação para preservar esse comportamento; não exigem registrar o tempo real gasto.

### Antecipar a próxima atividade para hoje

- Oferecer uma ação explícita para antecipar uma atividade prevista para uma data futura. Mostrar somente a próxima atividade elegível da sequência, com identificação e duração estimada, e perguntar se o usuário deseja realizá-la hoje.
- Essa escolha substitui a proposta anterior de perguntar quantos minutos ainda restam hoje. Ao aceitar, o usuário confirma que dispõe do tempo mostrado para aquela atividade; não precisa digitar novamente sua duração.
- Antecipar uma atividade por vez, sem permitir escolher uma posterior pulando a sequência. Respeitar as dependências, a revisão antes da próxima aula e os períodos de foco em projetos.
- Após aceitar, permitir repetir a ação para a próxima atividade elegível. Parar quando o usuário recusar ou não houver outra atividade elegível; não antecipar itens adicionais automaticamente.
- Para vídeos, a unidade é uma microaula inteira, com duração ajustada à velocidade escolhida. A revisão também permanece inteira. Blocos de projeto e provas devem seguir suas regras próprias de divisão e pré-requisitos.
- Mover a atividade para hoje e recalcular a distribuição futura, sem duplicá-la. Antecipar altera o planejamento, não registra conclusão; a execução continua sendo confirmada separadamente.
- Não alterar a rotina semanal por causa dessa escolha pontual. A confirmação autoriza tempo para a atividade selecionada, sem presumir quanto tempo livre real ainda existe no dia.
- A antecipação pode ser solicitada mesmo quando hoje tem disponibilidade planejada igual a zero. A confirmação autoriza a atividade selecionada para hoje, sem liberar automaticamente tempo para outras. A atividade pode vir de qualquer data futura, desde que seja a próxima da sequência; não precisa estar prevista para amanhã.

Ainda será preciso definir tecnicamente como representar e persistir a capacidade autorizada e as antecipações em recálculos repetidos no mesmo dia, sem duplicar minutos ou reutilizar tempo já consumido. Provas não recebem alocação de duração nesta fase e não podem ser realizadas antes de sua janela.

### Alternância de disciplinas e foco em projetos

- A alternância começa pela ordem de cadastro das disciplinas, sem uma configuração adicional para escolher a disciplina inicial. Decisão confirmada em 29/10/2026.
- Durante a preparação, alternar aulas completas entre as duas disciplinas: aula 1 de A, aula 1 de B, aula 2 de A, aula 2 de B. Uma aula pode ocupar vários dias, mas suas microaulas continuam indivisíveis entre datas.
- Dentro de cada aula, seguir a ordem de cadastro das microaulas, sem saltos. Depois da última microaula vem a revisão; só depois avançar para a próxima aula da alternância, respeitando as entradas em foco de projetos definidas abaixo. Decisão confirmada em 29/10/2026.
- Se a próxima atividade não couber na capacidade restante da data, manter a sobra livre e procurar uma data posterior em que ela caiba. Não preencher a sobra com uma microaula posterior, uma atividade de outra disciplina ou uma revisão fora de ordem. A antecipação para hoje também deve preservar essa sequência.
- A sequência de cada aula é: vídeos, revisão final obrigatória e então próxima aula, inclusive quando há troca de disciplina. Se a revisão ficar pendente, não antecipar a aula seguinte. Essa regra de planejamento não conclui a revisão automaticamente ao terminar os vídeos; o progresso continua dependendo do registro do usuário.
- A revisão é planejada inteira em uma única data, como as microaulas. Se exigir 10 minutos e restarem apenas 5 minutos não alocados, agendar em uma data posterior em que caiba, antes da próxima aula. O usuário pode aumentar explicitamente a disponibilidade da data e recalcular para tentar antecipá-la.
- Guardar separadamente a duração da revisão, maior que zero, e seu estado de conclusão. Concluir a revisão preserva a duração cadastrada e faz seu tempo pendente calculado ser zero. A velocidade de reprodução dos vídeos não altera a duração da revisão; sua conclusão continua exigindo todos os vídeos concluídos. Decisão confirmada em 29/10/2026; cadastro, cálculo e conclusão adaptados em 18/11/2026.
- Cada projeto recebe uma estimativa inicial de esforço, que pode ser distribuída entre dias respeitando a disponibilidade. Essa estimativa permite visualizar o planejamento futuro; não exige registrar minutos trabalhados nem atualizar diariamente o esforço restante.
- A reserva entre terminar a preparação e concluir o projeto corresponde à própria estimativa de execução distribuída pela rotina e pelas exceções. Não acrescentar uma margem independente em dias nesta fase. Exemplo: cinco horas podem ocupar três datas com duas horas, duas horas e uma hora de trabalho; a quantidade de datas depende da disponibilidade, não é um número fixo. Os requisitos precisam estar concluídos antes do início desse período, conforme a regra de início no dia seguinte. Decisão confirmada em 29/10/2026.
- No cadastro, permitir informar uma estimativa inicial para projetos fase 1 e outra para fase 2, reutilizando os valores nas respectivas entregas das disciplinas. Cada projeto conserva sua própria estimativa. Depois do cadastro, permitir editar a estimativa de um projeto específico sem modificar os demais; não implementar edição global de padrões nesta fase. Os valores iniciais são uma facilidade de preenchimento, não uma configuração compartilhada que altera retroativamente as entregas. Decisão de 02/11/2026. Não solicitar duração de provas para distribuição no calendário nesta fase.
- Após concluir os requisitos e atender às regras de agrupamento, iniciar o período de foco no projeto no dia seguinte, sem ocupar automaticamente a sobra do dia em que terminou a preparação. Manter o foco exclusivo até a conclusão registrada pelo usuário. Liberar não significa comprovar que o usuário começou a trabalhar. As atividades posteriores podem aparecer como previsão, mas continuam bloqueadas para execução.
- Quando os projetos da mesma fase exigirem quantidades diferentes de aulas, o primeiro a ter os pré-requisitos concluídos entra em foco exclusivo; após sua conclusão, retomar a alternância de conteúdos. Exemplo: Programação exige aulas 1–2 e Banco de Dados exige aulas 1–5.
- Quando os projetos da mesma fase exigirem a mesma quantidade de aulas, concluir a preparação de ambas as disciplinas antes de iniciar um período conjunto de foco nos dois projetos. Exemplo aprovado: A1, B1, A2, B2, depois projetos fase 1 de A e B.
- No período conjunto, somar os esforços estimados dos projetos. Dois projetos de três horas exigem seis horas da mesma disponibilidade pessoal; não duplicar a capacidade diária nem supor execução simultânea.
- No período conjunto, o detalhe diário mostrará um bloco como "Projetos — fase 1", com os minutos reservados, sem atribuir esse tempo a um projeto específico. O usuário decide em qual projeto trabalhar. O agrupamento é de planejamento e apresentação; cada projeto conserva seus pré-requisitos, estimativa, prazo e conclusão individual, sem exigir apontamento de minutos trabalhados.
- O bloco conjunto permanece em foco exclusivo até todos os projetos que o compõem estarem registrados como concluídos. Concluir apenas um não libera a retomada das aulas. Após a conclusão do último, planejar a continuidade a partir do dia seguinte; antecipar a próxima atividade para o mesmo dia depende de solicitação explícita. Decisão confirmada em 29/10/2026.
- A mesma quantidade de aulas não implica a mesma duração de estudo ou prazo; os pré-requisitos específicos de cada projeto continuam sendo respeitados.
- A estimativa orienta o plano, mas não conclui automaticamente um projeto. Se o período estimado terminar sem conclusão, manter o foco e sinalizar que a previsão posterior precisa ser revista, sem inventar um novo esforço restante.
- Após registrar a conclusão de um projeto em foco individual, recalcular a continuidade a partir do dia seguinte, usando a disponibilidade dessas datas. Para realizar a próxima atividade ainda no dia da conclusão, o usuário deve solicitar a antecipação explícita. Em foco conjunto, aplicar essa retomada somente após a conclusão de todos os projetos do bloco.
- Distribuir o trabalho tão cedo quanto permitirem a disponibilidade, a sequência e as restrições de liberação. Não adiar atividades apenas para aproximá-las do prazo regular. Mostrar a data prevista de conclusão, identificada como previsão; não é necessário acrescentar uma mensagem de término antecipado. Maior disponibilidade pode antecipar essa data, sem dispensar a conclusão registrada dos projetos nem ignorar janelas de realização de provas.
- Verificar conflitos com prazos ao aplicar o foco exclusivo e o agrupamento. Mostrar quais entregas não cabem, com prazo regular e data prevista quando calculável; se não houver espaço para estimar uma conclusão, informar essa limitação. Preservar a sequência aprovada, sem reordenar automaticamente atividades para resolver conflitos. O usuário escolhe ajustes manuais e solicita novo cálculo; não apresentar como viável um plano que ultrapasse as entregas.

### Provas: janela de realização e foco

- Cadastrar uma data de abertura e uma data limite regular para cada prova, em vez de fixar uma duração padrão de uma ou duas semanas para a janela.
- Mostrar as provas e suas janelas no planejamento. Dentro da janela, apresentar a prova como liberada para execução somente quando seus pré-requisitos de estudo estiverem concluídos; caso contrário, manter visíveis as pendências que impedem essa liberação. A abertura da janela não conclui nem pula conteúdos.
- O foco em provas depende da conclusão registrada pelo usuário, não da passagem da duração estimada. Cada prova tem seu próprio estado de conclusão.
- O usuário escolhe quando realizar cada prova dentro de sua janela, podendo fazer as duas no mesmo dia ou em dias diferentes. Mostrar ambas como disponíveis não significa reservar automaticamente a realização de ambas no dia de abertura.
- Mostrar somente a janela, os pré-requisitos e o estado de liberação/conclusão da prova, sem reservar minutos nem escolher uma data de realização pelo usuário. A previsão pode indicar quando a preparação termina, mas não afirmar que houve reserva de tempo suficiente para realizar a prova nem fornecer uma data prevista de realização como se estivesse agendada. Decisão confirmada em 02/11/2026.
- Se a janela regular terminar com uma prova pendente, informar o prazo encerrado, sem marcar conclusão nem transferir silenciosamente para outro período.
- O usuário relatou até três tentativas por prova, com aproveitamento da maior nota, e duração aproximada de uma hora por tentativa. Esses dados são contexto informado, não regras verificadas nem constantes a fixar no código. Como não haverá agendamento da realização das provas nesta fase, a duração e a possibilidade de interrupção não bloqueiam a implementação do escopo escolhido.
- Nesta fase, manter a interação simples, com foco e conclusão manual, sem agendamento automático de tentativas ou cálculo de notas. "Concluir prova" significa que o usuário encerrou essa prova no planejamento e não pretende realizar mais tentativas, mesmo que ainda existam tentativas disponíveis. Fazer uma tentativa, obter uma nota ou chegar ao fim da janela não conclui a prova automaticamente. Decisão confirmada em 29/10/2026.

## Exemplo manual de T02 — sequência de estudo

Cenário aprovado em 29/10/2026. Tempos dos vídeos já ajustados à velocidade escolhida. Banco de Dados foi cadastrado antes de Programação. Todas as atividades começam pendentes e não há projetos nem provas neste cenário.

Sequência: Banco de Dados (microaula 1: 20 min; microaula 2: 15 min; revisão: 10 min), depois Programação (microaula 1: 20 min; microaula 2: 10 min; revisão: 10 min).

| Dia | Disponibilidade | Atividades planejadas | Sobra |
| --- | ---: | --- | ---: |
| 1 | 30 min | Banco de Dados: microaula 1, 20 min | 10 min |
| 2 | 0 min | Nenhuma | 0 min |
| 3 | 40 min | Banco de Dados: microaula 2 e revisão, 25 min | 15 min |
| 4 | 30 min | Programação: microaulas 1 e 2, 30 min | 0 min |

A revisão de Programação, de 10 minutos, fica sem espaço no período. Há 100 minutos disponíveis e 85 minutos de atividades, mas as sobras não permitem pular a sequência nem dividir atividades. Portanto, a soma total suficiente não garante que tudo caiba.

Variação adicional de atraso:

- Se a primeira microaula não for concluída no dia 1, ao recalcular no dia 2 ela continua como primeira pendência; com zero minutos no dia 2, sua primeira data possível é o dia 3.

### Exemplo de recálculo com conclusões e atraso — aprovado

Aprovado pelo responsável pelo produto em 02/11/2026. Reutiliza a sequência e as disponibilidades da tabela anterior, sem mudar a velocidade, cadastrar exceções novas ou solicitar antecipações. O período termina no dia 4.

Os valores de sobra apresentados nos exemplos explicam a contabilidade do planejamento; não exigem uma coluna ou mensagem "sobra não utilizada" na interface. A apresentação final será definida no trabalho de interface do terminal.

1. No dia 1, o usuário conclui a microaula 1 de Banco de Dados (20 minutos). O dia 2 permanece sem disponibilidade.
2. No dia 3, estão previstas a microaula 2 de Banco de Dados (15 minutos) e sua revisão (10 minutos). O usuário conclui somente a microaula 2 e reabre ou recalcula o programa ainda no dia 3.
3. A microaula concluída preserva seus 15 minutos de alocação no dia. A revisão continua prevista para hoje; a próxima microaula de Programação (20 minutos) não é trazida automaticamente. A capacidade de 40 minutos do dia 3 permanece distribuída entre 15 minutos de atividade concluída, 10 de revisão pendente e 15 de sobra. Essas alocações são estimativas, não medições do tempo real gasto.
4. O usuário não conclui a revisão no dia 3. Ao abrir ou consultar o programa no dia 4, a revisão é a primeira pendência; não é necessário cadastrar uma exceção para o dia 3.

| Dia 4 após o recálculo | Minutos |
| --- | ---: |
| Revisão de Banco de Dados | 10 |
| Programação: microaula 1 | 20 |
| Total planejado / disponibilidade | 30 / 30 |

Ficam sem espaço até o fim do período: microaula 2 de Programação (10 minutos) e sua revisão (10 minutos). A revisão depende dessa microaula, portanto não pode ocupar uma posição anterior.

Verificações esperadas:

- As duas microaulas concluídas de Banco de Dados continuam concluídas e não voltam ao plano pendente.
- Reabrir no mesmo dia não recupera a capacidade alocada à atividade concluída nem puxa trabalho adicional automaticamente.
- A revisão atrasada precede as atividades de Programação no dia 4; a capacidade não utilizada do dia 3 não é transferida.
- Dos 85 minutos originais, 35 correspondem a atividades concluídas; restam 50 pendentes, sendo 30 planejados no dia 4 e 20 sem espaço no período. Um segundo recálculo sem mudanças no dia 4 preserva esse resultado.

### Disponibilidade e antecipação — exemplos aprovados

Aprovados em 02/11/2026. Duas alternativas independentes a partir do cenário inicial: a primeira microaula de Banco de Dados foi concluída no dia 1; hoje é o dia 2, originalmente com zero minutos. Não há outras conclusões registradas. Restam 65 minutos de atividades na sequência original.

**Alternativa A: alterar a disponibilidade do dia 2 para 40 minutos e recalcular.**

| Dia | Planejamento |
| --- | --- |
| 2 | Banco de Dados: microaula 2 (15 min) e revisão (10 min), total de 25 min |
| 3 | Programação: microaulas 1 e 2 (20 + 10 min) e revisão (10 min), total de 40 min |
| 4 | Sem atividades pendentes previstas |

**Alternativa B: antecipar apenas a próxima atividade para hoje, sem alterar a rotina ou cadastrar outra exceção.**

| Dia | Planejamento |
| --- | --- |
| 2 | Somente a microaula 2 de Banco de Dados, de 15 min, antecipada mediante confirmação |
| 3 | Revisão de Banco de Dados (10 min) e microaulas 1 e 2 de Programação (20 + 10 min), total de 40 min |
| 4 | Revisão de Programação, de 10 min |

Em ambas as alternativas, as datas posteriores são previsões condicionadas ao registro de progresso. A alteração da disponibilidade ou a antecipação não conclui nenhuma atividade. Na alternativa B, autorizar uma atividade não autoriza outras automaticamente, apesar da nova alocação no dia originalmente com zero minutos.

Uso esperado: antecipar quando surgir tempo livre hoje; cadastrar exceções para mudanças conhecidas de disponibilidade, como um compromisso futuro que reduza uma data de 40 para zero minutos. Se a disponibilidade dessa mesma data voltar a 40 minutos antes de ela chegar, substituir o valor da exceção e recalcular as pendências com a capacidade restaurada, sem alterar a rotina semanal ou o progresso. Isso não transfere automaticamente os 40 minutos para o dia anterior. O usuário também pode fazer novas antecipações, uma por vez, respeitando a sequência.

### Fluxo de aulas, projetos e provas — aprovado

Cenário reduzido aprovado em 02/11/2026, com 60 minutos disponíveis por dia, sem antecipações. Banco de Dados e Programação têm duas aulas cada, com 30 minutos por aula incluindo sua revisão. A fase 1 exige a aula 1 de cada disciplina; a fase 2 exige a aula 2. Cada projeto tem estimativa de 60 minutos, totalizando 120 minutos por bloco conjunto. Prazos regulares: fase 1 no dia 3 e fase 2 no dia 6. As provas abrem no dia 9 e encerram sua janela no dia 12.

| Dia | Planejamento esperado |
| --- | --- |
| 1 | Aula 1 de Banco de Dados e revisão, depois aula 1 de Programação e revisão: 60 min |
| 2 | Projetos — fase 1: 60 min previstos |
| 3 | Projetos — fase 1: 60 min previstos; prazo regular da fase 1 |
| 4 | Aula 2 de Banco de Dados e revisão, depois aula 2 de Programação e revisão: 60 min |
| 5 | Projetos — fase 2: 60 min previstos |
| 6 | Projetos — fase 2: 60 min previstos; prazo regular da fase 2 |
| 7 e 8 | Sem atividades planejadas; aguardando abertura das provas |
| 9 a 12 | Provas liberadas enquanto pendentes e dentro da janela, sem reserva de minutos |

Premissa do cenário: o usuário registra as conclusões das aulas nos dias indicados e conclui individualmente ambos os projetos de cada bloco até seu último dia previsto. O usuário escolhe a divisão do trabalho entre os projetos, sem apontamento de minutos.

As aulas do dia 4 são apenas previsão enquanto houver projeto da fase 1 pendente. Sua liberação depende da conclusão de ambos os projetos; os 120 minutos estimados não registram essa conclusão. Cada bloco começa no dia seguinte ao término da preparação, e as aulas são retomadas no dia seguinte à conclusão do bloco, salvo antecipação explícita. As provas conservam conclusões individuais e sua liberação depende da janela e dos pré-requisitos; não são automaticamente concluídas no dia 12.

### Projeto pendente após a previsão e o prazo — aprovado

Variação do fluxo anterior, aprovada em 02/11/2026: no início do dia 4, somente um dos projetos da fase 1 foi registrado como concluído. O outro continua pendente, apesar da previsão de término e do prazo regular no dia 3.

- Preservar o projeto já concluído; manter o foco exclusivo no projeto restante e mostrar que seu prazo regular encerrou.
- As aulas anteriormente previstas para o dia 4 permanecem bloqueadas. A estimativa esgotada não libera a continuidade nem comprova trabalho realizado.
- Não inventar um esforço restante, uma nova data de conclusão do projeto ou um prazo extra. Identificar a previsão posterior como desatualizada/condicionada à conclusão, sem apresentar datas antigas como um plano atual viável.
- Se o usuário registrar a conclusão do projeto restante no dia 4, recalcular então a continuidade com início no dia 5. O recálculo pode ser apresentado imediatamente após o registro; não é preciso aguardar a meia-noite para consultar a nova previsão. Realizar a próxima atividade no próprio dia 4 exige antecipação explícita.
- A previsão recalculada precisa verificar novamente os prazos seguintes. Concluir o projeto atrasado não altera seu prazo original nem garante que as próximas entregas caibam.

As estimativas de projetos permitem visualizar o período, reservar esforço e verificar prazos; não medem a execução nem concluem projetos. A visão pode mostrar o término previsto dos conteúdos e projetos e as janelas das provas. Como as provas não são agendadas, não apresentar essa previsão como garantia da data de conclusão de todo o trimestre.

## Pendências de produto e implementação

Detalhes técnicos a resolver antes de T04 e T05, com comportamento de produto já definido:

- Adaptação de revisões implementada em 18/11/2026: minutos antigos positivos tornam-se a duração com `concluida=False`; zero exige a duração original informada pelo usuário, preservando `concluida=True`. A estrutura nova contém ID, duração e conclusão. A conversão ocorre em memória antes do menu e é gravada no momento habitual, após uma ação válida; respostas inválidas não sobrescrevem o arquivo. Revisões já adaptadas mantêm ID, duração e progresso sem novas perguntas.
- Definir tecnicamente como representar e persistir as alocações do dia e as antecipações, sem reutilizar a capacidade de atividades concluídas. O comportamento esperado está definido acima; não é necessário medir o tempo real gasto.

Antes de T09–T11:

- Definir os pré-requisitos específicos de cada entrega no cadastro. A sequência aprovada permanece válida quando houver conflitos de prazos; informar inviabilidade e permitir ajustes manuais, sem priorização automática que altere essa sequência.

Antes de T08:

- Se uma microaula concluída for reaberta depois da revisão, o que deve acontecer com a revisão? A duração original já é preservada separadamente, mas a regra de reabertura ainda precisa ser definida.

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

**Estado:** concluída em 02/11/2026, após validação global do MVP pelo responsável pelo produto. Aprovados os exemplos de estudo, recálculo com conclusões e atraso, disponibilidade/antecipação, fluxo completo de aulas/projetos/provas e projeto pendente após a previsão e o prazo. Na confirmação final, foi mantida a regra anterior de projetos: foco individual quando os requisitos diferem e agrupamento dos projetos da mesma fase quando exigem a mesma quantidade de aulas, aguardando a preparação de ambos. Revisão independente concluída: cálculos conferidos e nenhum bloqueador identificado para T03–T05; referências antigas corrigidas. A conclusão da T02 valida o escopo e o comportamento esperado, não a implementação. Detalhes de persistência e migração serão resolvidos na implementação; correção de conclusão após revisão está vinculada a T08.

**Aceite:**
- Resolver as decisões de divisão, ordem, revisão e data de referência listadas acima.
- Montar um exemplo pequeno de duas disciplinas compartilhando os mesmos minutos diários, com resultado esperado por data.
- Incluir um dia com zero, uma atividade concluída e uma situação que não cabe; calcular o resultado esperado sem usar o algoritmo a ser desenvolvido.
- Confirmar o que encerra a fase Terminal e quais reservas entram nela.
- Antes de encerrar T02, revisar o conjunto das regras e apresentar uma visão consolidada do MVP Terminal: fluxo completo de uso, funcionalidades incluídas e excluídas, distinção entre previsão e execução, exemplos esperados e limites. Validar esse conjunto com o responsável pelo produto; não considerar aprovações isoladas como substitutas dessa revisão final.

**Dependências:** nenhuma. Não exige uma funcionalidade nova.

### T03 — Representar atividades pendentes para o agendamento

**Estado:** em andamento. Microaulas possuem IDs persistidos, reutilizados nas atividades pendentes. O cadastro das revisões já separa ID, duração original e conclusão, com adaptação dos arquivos antigos e uso pelo cálculo e progresso. Ainda faltam vínculos das atividades com aula/disciplina, geração das atividades de revisão e composição da sequência. A lista de atividades ainda não está integrada ao terminal nem à distribuição por datas. Validação local deste incremento: 156 testes passando.

**Problema:** o total de minutos não informa qual vídeo ou revisão deve ser realizado em cada data.

**Incremento de 17/11/2026:** cada atividade de microaula gerada contém `microaula_id`, copiado do ID já atribuído no cadastro. Regerar as pendências preserva o vínculo mesmo com títulos iguais ou mudança de velocidade, excluindo as concluídas sem removê-las do cadastro. A função exige IDs nas microaulas pendentes; não os gera. Ainda não há conclusão pelo ID no terminal nem integração dessa lista ao cronograma. Permanecem pendentes os vínculos com aula/disciplina, revisões e composição da sequência.

**Incremento de 05/11/2026:** adicionada `atribuir_ids_microaulas`, em `cadastro.py`. Antes da gravação já existente no terminal, microaulas sem a chave `id` recebem um UUID convertido em texto; IDs existentes e demais dados são preservados. Isso atende cadastros novos e antigos, sem gravar durante a leitura nem alterar o arquivo antes de uma ação válida. A função preenche chaves ausentes; ainda não valida IDs fornecidos externamente. Os vínculos das atividades geradas com esses IDs, aula/disciplina, as revisões e a composição da sequência continuam pendentes.

**Aceite:**
- Produzir atividades identificáveis, vinculadas à aula e à disciplina, com duração restante e dependências conforme T02.
- Excluir atividades concluídas e incluir revisão pendente uma única vez.
- Manter o cadastro e as regras de cálculo existentes; definir referências que continuem válidas quando o cadastro for editado.
- Para microaulas, manter a duração original separada da estimativa de reprodução e do estado de conclusão; não introduzir progresso parcial nesta fase.

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
- Manter pendências de dias passados na sequência e redistribuí-las de hoje em diante, sem transferir a capacidade não utilizada desses dias.
- Registrar uma conclusão de hoje não deve acrescentar automaticamente outra atividade ao dia nem liberar novamente sua capacidade planejada, inclusive em recálculos repetidos e após reabrir o programa.
- Uma exceção de zero retirar a capacidade apenas da data correspondente; redistribuir o trabalho restante conforme a regra aprovada.
- Aceitar uma exceção de zero para hoje mesmo após uma conclusão, preservando o progresso e redistribuindo somente pendências, sem capacidade restante negativa.
- Ao abrir o programa ou consultar/recalcular o plano após a mudança de dia em Brasília, redistribuir pendências a partir da nova data, sem exigir uma exceção para o dia perdido ou um serviço em segundo plano.
- Não marcar tarefas como feitas pela passagem do tempo, não contar dias passados como capacidade futura e não aumentar a velocidade automaticamente.
- Mesmas entradas produzirem o mesmo resultado; se não houver espaço, informar as pendências que ficaram de fora.

**Dependências:** T04 e decisões de T02. Não exige criar um serviço em segundo plano nem guardar versões anteriores do cronograma.

### T06 — Consultar e recalcular o cronograma pelo terminal

**Aceite:**
- Oferecer uma ação para consultar o plano com data, disciplina, aula, atividade, minutos utilizados e limite do dia.
- Permitir consultar o resumo do período e o detalhe de uma data, incluindo reservas e prazos quando T09–T11 estiverem implementadas.
- Permitir recalcular após registrar progresso ou modificar a disponibilidade, reaproveitando T05.
- Permitir antecipar somente a próxima atividade elegível para hoje, mostrando sua duração e solicitando confirmação a cada item, conforme as regras de T02.
- Diferenciar atividade planejada de atividade concluída e mostrar as pendências sem espaço.
- Explicar o impacto do recálculo: o que permanece pendente, sua nova distribuição e eventuais entregas comprometidas.
- Mostrar a data de referência e informar quando não houver pendências.
- Quando os conteúdos e projetos estiverem concluídos e restar apenas uma prova cuja janela ainda não abriu, mostrar os dias intermediários como "Sem atividades planejadas" e indicar a data de abertura da prova. Não criar atividades para preencher esse intervalo nem apresentar a prova como concluída ou antecipável antes da abertura. Mostrar a janela e a liberação, sem reservar a duração da prova.

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
- Incluir o dia final no planejamento e distinguir uma conclusão prevista no próprio prazo de outra prevista após ele. Para projetos, apresentar o limite de 23h59 no horário de Brasília e reconhecer o prazo encerrado a partir do dia seguinte.
- Para provas, registrar também a abertura da janela regular e distinguir prova aguardando abertura, bloqueada por pré-requisitos, liberada, concluída e pendente com prazo encerrado na apresentação, sem exigir uma representação técnica específica desses estados.
- Não agendar a duração das provas nem declarar capacidade reservada para sua realização; distinguir a previsão de término da preparação da escolha de quando realizar a prova, que fica com o usuário.
- Permitir consultar e corrigir essas informações pelo terminal e recuperá-las em outra execução.
- Uma aula usada por mais de uma entrega deve continuar sendo o mesmo conteúdo, sem duplicar seu tempo.
- Confirmar quais revisões e atividades de execução pertencem a cada entrega.

**Dependências:** T02, T03 e T08. Não calcular notas nem penalidades nesta issue.

### T10 — Representar as reservas de execução dos projetos e as revisões

**Estado:** reserva de execução dos projetos definida pela estimativa de esforço; sem margem independente em dias. Exercícios excluídos desta fase em 02/11/2026.

**Aceite:**
- Reservar a estimativa de esforço dos projetos após a preparação, distribuindo seus minutos pela disponibilidade de cada data, sem acrescentar uma margem independente em dias. Considerar esse período ao verificar o cumprimento do prazo regular.
- Reutilizar valores iniciais por fase no cadastro, armazenando a estimativa individual de cada projeto e permitindo alterá-la sem modificar os outros projetos.
- Conciliar reservas de duas disciplinas sem duplicar capacidade e explicitar quando uma reserva for inviável.
- Evitar contar novamente a revisão da aula como outra atividade idêntica.

**Dependências:** T02 e T09; unidades e prioridades precisam estar decididas antes do código.

### T11 — Considerar prazos e reservas na distribuição e no recálculo

**Aceite:**
- Evoluir T04 e T05 para respeitar os prazos, dependências e reservas aprovados.
- Compartilhar a capacidade diária entre entregas e disciplinas, usando o critério de prioridade definido.
- Demonstrar um caso em que o total do período é suficiente, mas uma entrega antecipada não pode ser cumprida.
- Exibir a entrega comprometida e o trabalho restante sem ocultar excesso nem trocar automaticamente o prazo regular por um prazo com penalidade.
- Identificar a situação de cada entrega separadamente, com seu prazo regular e a data prevista quando calculável; não declarar todas inviáveis se apenas uma estiver comprometida.
- Oferecer ajustes manuais de disponibilidade, velocidade e estimativa de um projeto específico, sem recomendações automáticas nem mudanças silenciosas. Permitir sair preservando os dados mesmo quando o plano continuar inviável.
- Recalcular após uma exceção ou atualização de progresso mantendo essas mesmas regras.
- Mostrar datas previstas de conclusão tão cedo quanto as regras permitirem, distinguindo previsão de liberação para execução e respeitando a retomada no dia seguinte à conclusão de projetos individuais, salvo antecipação explícita.

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

T01 está concluída localmente e T02 teve seu escopo validado pelo responsável pelo produto. Para o foco no recalculador, a próxima sequência técnica é T03 → T04 → T05 → T06. T07 e T08 tornam o uso recorrente mais prático e podem ser priorizadas antes. T09 → T10 → T11 completam o planejamento por entregas. T12 verifica o conjunto aprovado.

API, interface web, autenticação, PostgreSQL, Docker, nuvem, importação de PDFs e integração com o portal não são planejados neste backlog. Notas, faltas e regras de penalidade também ficam fora da proposta desta fase, conforme os limites já registrados; sua inclusão exigiria uma decisão explícita de escopo.

Reorganizar pastas ou aplicar padrões de projeto não é condição automática para concluir uma issue. Fazer refatorações quando ajudarem uma mudança concreta, sem reconstruir o que já funciona.
