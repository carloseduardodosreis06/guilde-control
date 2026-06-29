# utils/helpers.py

def datetime import datetime

def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

def hora_atual():
    return datetime.now().strftime("%H:%M")

def data_hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def formatar_nome(nome):
    return nome.strip().title()

def formatar_telefone(telefone):
    telefone = telefone.replace(" ", "").replace("-", "")
    return telefone

def formatar_pontos(valor):
    try:
        return int(valor)
    except:
        return 0

def mensagem_sucesso(msg):
    return{
        "status": "sucesso",
        "mensagem": msg
    }

def mensagem_erro(msg):    
    return{
        "status": "erro",
        "mensagem": msg
    }