# services/pix_service.py

from config import PIX_CHAVE

pagamentos = []


def criar_pagamento(nome, valor, status="Pendente"):
    pagamentos.append({
        "nome": nome,
        "valor": valor,
        "status": status
    })


def listar_pagamentos():
    return pagamentos


def confirmar_pagamento(nome):
    for pagamento in pagamentos:
        if pagamento["nome"] == nome:
            pagamento["status"] = "Pago"
            return True

    return False


def remover_pagamento(nome):
    global pagamentos

    pagamentos = [
        pagamento for pagamento in pagamentos
        if pagamento["nome"] != nome
    ]


def total_recebido():
    total = 0

    for pagamento in pagamentos:
        if pagamento["status"] == "Pago":
            total += pagamento["valor"]

    return total

def obter_pix():
    return {
        "chave": PIX_CHAVE
    }