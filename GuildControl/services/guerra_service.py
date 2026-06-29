# services/guerra_service.py

guerras = []


def adicionar_guerra(data, inimigo, kills, colocacao):
    guerras.append({
        "data": data,
        "inimigo": inimigo,
        "kills": kills,
        "colocacao": colocacao
    })


def listar_guerras():
    return guerras


def total_kills():
    total = 0

    for guerra in guerras:
        total += guerra["kills"]

    return total


def atualizar_guerra(data, kills, colocacao):
    for guerra in guerras:
        if guerra["data"] == data:
            guerra["kills"] = kills
            guerra["colocacao"] = colocacao
            return True

    return False


def remover_guerra(data):
    global guerras

    guerras = [
        guerra for guerra in guerras
        if guerra["data"] != data
    ]
