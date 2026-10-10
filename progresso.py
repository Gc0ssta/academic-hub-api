def marcar_microaula_concluida(
    aula: dict,
    indice_microaula: int,
) -> None:
    
    if type(indice_microaula) is not int:
        raise TypeError("O indice da microaula precisa ser um numero inteiro")

    if indice_microaula < 0 or indice_microaula >= len(aula["microaulas"]):
        raise IndexError("Nao informou um indice valido")
    
    aula["microaulas"][indice_microaula]["concluida"] = True