import json

def salvar_aulas(aulas: list[dict], caminho: str) -> None:
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(aulas, arquivo, ensure_ascii=False, indent=4)

def carregar_aulas(caminho: str) -> list[dict]:
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []