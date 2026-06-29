# services/horas_service.py

horas_jogadas = []


def adicionar_horas(jogador, horas):
    horas_jogadas.append({
        "jogador": jogador,
        "horas": horas
    })


def listar_horas():
    return horas_jogadas


def total_horas():
    total = 0

    for jogador in horas_jogadas:
        total += jogador["horas"]

    return total


def atualizar_horas(jogador, horas):
    for item in horas_jogadas:
        if item["jogador"] == jogador:
            item["horas"] = horas
            return True

    return False


def remover_jogador(jogador):
    global horas_jogadas

    horas_jogadas = [
        item for item in horas_jogadas
        if item["jogador"] != jogador
    ]
