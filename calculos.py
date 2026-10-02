def calcular_tempo_video(
    duracao_minutos: float, 
    velocidade: float
) -> float:

    if velocidade <= 0:
        raise ValueError("A velocidade deve ser maior que zero.")

    if duracao_minutos <= 0:
        raise ValueError("A duração do video deve ser maior que zero.")
    
    return duracao_minutos / velocidade

def calcular_tempo_aula(
    duracao_microaula: float, 
    quantidade_microaulas: int, 
    velocidade: float, 
    tempo_revisao: float
) -> float:
    """Calcula o tempo da aula em minutos, incluindo a revisão.

    Considera microaulas com a mesma duração e velocidade.
    A quantidade informada deve ser um inteiro maior que zero.
    """
    if tempo_revisao < 0:
        raise ValueError("O tempo de revisão não pode ser um número negativo")

    if type(quantidade_microaulas) is not int:
        raise TypeError("A quantidade de micro aulas precisa ser um número inteiro")

    if quantidade_microaulas <= 0:
        raise ValueError("A quantidade de micro aulas precisa ser maior que zero")

    tempo_microaula = calcular_tempo_video(duracao_microaula, velocidade)

    tempo_aula = tempo_microaula * quantidade_microaulas

    aula_revisao = tempo_aula + tempo_revisao

    return aula_revisao

def cabe_no_tempo(
    tempo_necessario: float, 
    tempo_disponivel: float
) -> bool:

    if tempo_necessario < 0:
        raise ValueError("O tempo necessario não pode ser um número negativo")

    if tempo_disponivel < 0:
        raise ValueError("O tempo disponivel não pode ser um número negativo")

    return tempo_disponivel >= tempo_necessario

def calcular_microaulas_pendentes(
    quantidade_total: int, 
    quantidade_concluida: int
) -> int:

    if type(quantidade_total) is not int or type(quantidade_concluida) is not int:
        raise TypeError("A quantidade de micro aulas precisa ser numeros inteiros")
    
    if quantidade_total <= 0:
        raise ValueError("A quantidade total deve ser maior que zero.")

    if quantidade_concluida < 0:
        raise ValueError("A quantidade concluída não pode ser negativa.")

    if quantidade_concluida > quantidade_total:
        raise ValueError("A quantidade concluída não pode superar o total.")

    return quantidade_total - quantidade_concluida

def calcular_tempo_restante_aula(
    duracao_microaula: float,
    quantidade_total: int,
    quantidade_concluida: int,
    velocidade: float,
    tempo_revisao_pendente: float,
) -> float:
    if tempo_revisao_pendente < 0:
        raise ValueError("tempo de revisao pendente nao pode ser um numero negativo")

    microaulas_pendentes = calcular_microaulas_pendentes(quantidade_total, quantidade_concluida)

    duracao_microaulas = calcular_tempo_video(duracao_microaula, velocidade)

    return (microaulas_pendentes * duracao_microaulas) + tempo_revisao_pendente