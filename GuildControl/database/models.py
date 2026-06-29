# database/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    plano = db.Column(db.String(50), default="Grátis")


class Guilda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    lider = db.Column(db.String(100), nullable=False)


class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(100), nullable=False)
    line = db.Column(db.String(50), nullable=False)
    horas = db.Column(db.Integer, default=0)
    pontos = db.Column(db.Integer, default=0)


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="Pendente")
