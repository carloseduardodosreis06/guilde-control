# services/ranking_service.py

ranking = []


def adicionar_line(nome, pontos):
    ranking.append({
        "nome": nome,
        "pontos": pontos
    })


def listar_ranking():
    return sorted(
        ranking,
        key=lambda line: line["pontos"],
        reverse=True
    )


def atualizar_pontos(nome, pontos):
    for line in ranking:
        if line["nome"] == nome:
            line["pontos"] = pontos
            return True
    return False


def remover_line(nome):
    global ranking
    ranking = [
        line for line in ranking
        if line["nome"] != nome
    ]
