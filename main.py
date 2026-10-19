from calculos import calcular_tempo_total_pendente, cabe_no_tempo, calcular_tempo_disponivel_total

from armazenamento import carregar_aulas, salvar_aulas

from progresso import marcar_microaula_concluida, marcar_revisao_concluida

from datetime import date

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

def ler_disponibilidades_diarias() -> list[float]:
    quantos_dias = int(input("Quantos dias deseja considerar? "))
    if quantos_dias <= 0:
        raise ValueError("A quantidade de dias deve ser maior que zero.")

    lista = []

    for dia in range(1, quantos_dias + 1):
        minutos = float(input(f"Quantos minutos estão disponíveis no dia {dia}? "))
        if minutos < 0:
            raise ValueError("Nao e possivel escolher uma numeracao negativa aqui")
        lista.append(minutos)

    return lista

def ler_data(mensagem: str) -> date:
    data = date.fromisoformat(input(mensagem))
    return data

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

        velocidade_videos = float(input("Qual velocidade dos videos? "))
        disponibilidades = ler_disponibilidades_diarias()
        tempo_disponivel = calcular_tempo_disponivel_total(disponibilidades)

        tempo_restante = calcular_tempo_total_pendente(aulas, velocidade_videos)
        atividade_cabe = cabe_no_tempo(tempo_restante, tempo_disponivel)

        salvar_aulas(aulas, "aulas.json")
        
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





