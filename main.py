from calculos import calcular_tempo_total_pendente, cabe_no_tempo

from armazenamento import carregar_aulas, salvar_aulas

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

        velocidade_videos = float(input("Qual velocidade dos videos? "))
        tempo_disponivel = float(input("Quantos minutos você tem disponíveis? "))

        tempo_restante = calcular_tempo_total_pendente(aulas, velocidade_videos)
        atividade_cabe = cabe_no_tempo(tempo_restante, tempo_disponivel)

        salvar_aulas(aulas, "aulas.json")
        
    except (ValueError, OSError) as erro:
        print("Não foi possível calcular:", erro)
    else:
        print("Tempo restante:", tempo_restante, "minutos")
        
        if atividade_cabe:
            print("As atividades pendentes cabem no tempo disponível.")
        else:
            print("As atividades pendentes não cabem no tempo disponível.")

if __name__ == "__main__":
    main()





