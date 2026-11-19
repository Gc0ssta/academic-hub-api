from uuid import uuid4


def criar_revisao(duracao_minutos: float, concluida: bool = False) -> dict:
    """Cria uma revisão com identidade, duração original e conclusão separadas."""
    if duracao_minutos <= 0:
        raise ValueError("A duração da revisão deve ser maior que zero.")
    if type(concluida) is not bool:
        raise TypeError("A conclusão da revisão deve ser um booleano.")
    return {
        "id": str(uuid4()),
        "duracao_minutos": duracao_minutos,
        "concluida": concluida,
    }


def adaptar_revisao_antiga(
    aula: dict,
    duracao_original: float | None = None,
) -> None:
    """Converte o campo antigo em memória; não lê entradas nem grava arquivos.

    Para zero minutos pendentes, exige a duração informada pelo usuário e
    preserva a conclusão. Revisões já adaptadas não são modificadas.
    """
    if "revisao" in aula:
        return

    minutos_pendentes = aula["tempo_revisao_pendente"]
    if minutos_pendentes < 0:
        raise ValueError("O tempo de revisão pendente não pode ser negativo.")

    if minutos_pendentes == 0:
        if duracao_original is None:
            raise ValueError("Informe a duração original da revisão concluída.")
        revisao = criar_revisao(duracao_original, concluida=True)
    else:
        revisao = criar_revisao(minutos_pendentes, concluida=False)

    aula["revisao"] = revisao
    del aula["tempo_revisao_pendente"]


def atribuir_ids_microaulas(aulas: list[dict]) -> None:
    """Adiciona IDs às microaulas que ainda não possuem a chave id.

    Modifica o cadastro recebido, preservando os IDs e demais dados existentes.
    A gravação em arquivo fica por conta de quem chama a função.
    """
    for aula in aulas:
        for microaula in aula["microaulas"]:
            if "id" not in microaula:
                microaula["id"] = str(uuid4())
