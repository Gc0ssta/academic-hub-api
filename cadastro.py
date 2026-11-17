from uuid import uuid4


def atribuir_ids_microaulas(aulas: list[dict]) -> None:
    """Adiciona IDs às microaulas que ainda não possuem a chave id.

    Modifica o cadastro recebido, preservando os IDs e demais dados existentes.
    A gravação em arquivo fica por conta de quem chama a função.
    """
    for aula in aulas:
        for microaula in aula["microaulas"]:
            if "id" not in microaula:
                microaula["id"] = str(uuid4())
