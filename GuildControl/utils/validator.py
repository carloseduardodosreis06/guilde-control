# utils/validator.py

import re

def validar_email(email):
    padrao = r"^[/w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None

def validar_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"[0-9]", senha):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False
    return True

def validar_telefone(telefone):
    telefone = re.sub(r"/D", "", telefone)
    return len(telefone) in [10, 11]

def validar_nick(nick):
    return len(nick.strip()) >= 3

def  validar_id_jogo(id_jogo):
    return str(id_jogo).isdigit() 

def validar_line(line):
    return str(line).isdigit() 

def validar_pontos(pontos):
    try:
        int(pontos)
        return True
    except ValueError:
        return False