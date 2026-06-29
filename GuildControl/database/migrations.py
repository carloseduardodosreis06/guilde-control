# database/migrations.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco de dados.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("Banco de dados criado com sucesso!")
        print("🥰 Obrigado por utilizar o GuildControl.")
        print('📔 "Entrega o teu caminho ao senhor; confia nele, e ele tudo fara." - Salmos 37:5')

def reset_db(db):
    """
    Remover todas as tabelas e recria o banco.
    Atenção: apaga todos os dados.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Banco de dados reiniciado com sucesso!")