from calculos import calcular_tempo_total_pendente, cabe_no_tempo, calcular_tempo_disponivel_total

from armazenamento import carregar_aulas, salvar_aulas

from progresso import marcar_microaula_concluida, marcar_revisao_concluida

from datetime import date

from planejamento import gerar_disponibilidades_periodo

def ler_microaula() -> dict:

    titulo = str(input("qual o titulo da microaula? "))

    duracao_minutos = float(input("quantos minutos dura a microaula? "))
    if duracao_minutos <= 0:
        raise ValueError("A duração da microaula não pode ser um numero negativo ou zero")
    
    concluida_ou_nao = str(input("Se essa microaula foi concluida digite s se nao digite n: ")).lower()
    if concluida_ou_nao != "s" and concluida_ou_nao != "n":
        raise ValueError("Digite s para concluída ou n para não concluída.")
    
    if concluida_ou_nao == "s":
        concluida_ou_nao = True
    else:
        concluida_ou_nao = False

    dicionario = {
    "titulo": titulo,
    "duracao_minutos": duracao_minutos,
    "concluida": concluida_ou_nao,
    }

    return dicionario

def ler_aula() -> dict:
    disciplina = str(input("Qual a disciplina da aula? "))

    titulo = str(input("Qual o titulo da aula? "))

    quantidade_microaulas = int(input("Quantas microaulas possui? "))
    if quantidade_microaulas <= 0:
        raise ValueError("A quantidade de microaulas precisa ser um valor maior que zero")

    microaulas = []

    for _ in range(quantidade_microaulas):
        microaula = ler_microaula()
        microaulas.append(microaula)

    tempo_revisao_pendente = float(input("Quantos minutos de revisao pendente? "))
    if tempo_revisao_pendente < 0:
        raise ValueError("O tempo de revisao nao pode ser negativo")

    aula = {
        "disciplina": disciplina,
        "titulo": titulo,
        "microaulas": microaulas,
        "tempo_revisao_pendente": tempo_revisao_pendente
    }

    return aula

def selecionar_aula(aulas: list[dict]) -> dict:
    for numero, aula in enumerate(aulas, start=1):
        print(numero, "-", aula["disciplina"], "-", aula["titulo"])

    numero_escolhido = int(input("Qual aula deseja selecionar? "))

    if numero_escolhido < 1 or numero_escolhido > len(aulas):
        raise ValueError("Nao existe aulas relacionadas com esse valor")

    return aulas[numero_escolhido - 1]

def selecionar_indice_microaula(aula: dict) -> int:
    
    microaulas = aula["microaulas"]

    for numero, microaula in enumerate(microaulas, start=1):
        print(numero, "-", microaula["titulo"])

    numero_escolhido = int(input("Qual microaula deseja selecionar? "))

    if numero_escolhido < 1 or numero_escolhido > len(microaulas):
        raise ValueError("Não existe microaula com esse número.")

    return numero_escolhido - 1

def ler_data(mensagem: str) -> date:
    data = date.fromisoformat(input(mensagem))
    return data

def ler_rotina_semanal() -> dict[int, float]:
    dias_semana = [
        "segunda-feira", 
        "terca-feira", 
        "quarta-feira", 
        "quinta-feira", 
        "sexta-feira", 
        "sabado", 
        "domingo",
    ]

    rotina_semanal = {}

    for numero_dia, nome_dia in enumerate(dias_semana):
        minutos = float(input(f"Quantos minutos disponiveis para faculdade voce tem no dia de {nome_dia}? "))

        if minutos < 0:
            raise ValueError("O Valor escolhido nao pode ser numero negativo")

        rotina_semanal[numero_dia] = minutos

    return rotina_semanal

def ler_excecoes() -> dict[date, float]:
    quantidade = int(input("Quantas excecoes voce pretende informar: "))
    if quantidade < 0:
        raise ValueError("A quantidade de exceções não pode ser negativa.")

    excecoes = {}

    for _ in range(quantidade):
        data_excecao = ler_data("Informe a data da excecao no formato AAAA-MM-DD : ")
        minutos = float(input("Quantos minutos voce tera disponivel nessa data? "))
        if minutos < 0:
            raise ValueError("Os minutos da exceção não podem ser negativos.")
        
        excecoes[data_excecao] = minutos

    return excecoes

def main() -> None:
    try:
        aulas = carregar_aulas("aulas.json")

        if not aulas:
            quantidade_aulas = int(input("Quantas aulas deseja informar? "))
            if quantidade_aulas <= 0:
                raise ValueError("A quantidade de aulas deve ser maior que zero.")

            for _ in range(quantidade_aulas):
                aula = ler_aula()
                aulas.append(aula)

        print("0 - Apenas calcular o tempo pendente")
        print("1 - Marcar uma microaula como concluída")
        print("2 - Marcar uma revisão como concluída")

        opcao = input("Escolha uma opção: ")

        if opcao != "0" and opcao != "1" and opcao != "2":
            raise ValueError("Voce nao digitou um valor valido")

        if opcao == "1":
            aula_selecionada = selecionar_aula(aulas)
            indice = selecionar_indice_microaula(aula_selecionada)
            marcar_microaula_concluida(aula_selecionada, indice)
            
        elif opcao == "2":
            aula_selecionada = selecionar_aula(aulas)
            marcar_revisao_concluida(aula_selecionada)

        salvar_aulas(aulas, "aulas.json")

        velocidade_videos = float(input("Qual velocidade dos videos? "))

        data_inicio = ler_data("Informe a data de inicio no formato (AAAA-MM-DD): ")
        data_fim = ler_data("Informe a data final no formato (AAAA-MM-DD): ")
        rotina_semanal = ler_rotina_semanal()
        excecoes = ler_excecoes()

        disponibilidades = gerar_disponibilidades_periodo(
            data_inicio=data_inicio,
            data_fim=data_fim,
            rotina_semanal=rotina_semanal,
            excecoes=excecoes,
        )

        minutos_dia = []

        for dia in disponibilidades:
            minutos_dia.append(dia["minutos_disponiveis"])

        tempo_disponivel = calcular_tempo_disponivel_total(minutos_dia)

        tempo_restante = calcular_tempo_total_pendente(aulas, velocidade_videos)
        atividade_cabe = cabe_no_tempo(tempo_restante, tempo_disponivel)
        
    except (ValueError, OSError) as erro:
        print("Não foi possível calcular:", erro)
    else:
        print("Tempo restante:", tempo_restante, "minutos")
        print("Tempo disponível no período:", tempo_disponivel, "minutos")
        print("Esta comparação considera apenas o total de minutos, sem distribuir as atividades por dia.")
        
        if atividade_cabe:
            print("As atividades pendentes cabem no tempo disponível.")
        else:
            print("As atividades pendentes não cabem no tempo disponível.")

if __name__ == "__main__":
    main()





