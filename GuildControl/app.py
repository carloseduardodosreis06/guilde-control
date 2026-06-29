import os, qrcode, io, base64
from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from database.models import db, Usuario, Guilda, Membro, Pagamento

# Importação dos Blueprints organizados nas subpastas
from routes.auth import auth
from routes.guildas import guildas
from routes.membros import membros

app = Flask(__name__)

# Configurações do Banco de Dados SQLite local permanentemente
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///guildcontrol.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados integrado ao app Flask
db.init_app(app)

# Cria as tabelas do banco de dados automaticamente se não existirem
with app.app_context():
    db.create_all()

# Registro dos Blueprints no servidor Flask
app.register_blueprint(auth)
app.register_blueprint(guildas)
app.register_blueprint(membros)

# Dados de teste para compatibilidade com o front-end
USUARIO_LOGADO = {
    "username": "GuildMaster_Pro",
    "plano_ativo": "Gratuito",
    "expiracao_plano": None
}

# --- ROTAS PRINCIPAIS DO SISTEMA ---

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/pagamentos")
def pagamentos():
    minha_chave_pix= "ce023233@gmail.com"
    img = qrcode.make(minha_chave_pix)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return render_template("pagamentos.html", chave_pix=minha_chave_pix, qrcode_image=qr_base64)

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/ranking")
def ranking():
    return render_template("ranking.html")

# --- ROTA DE PAGAMENTO INTEGRADA AO BANCO DE DADOS ---

@app.route('/verificar-pagamento', methods=['POST'])
def verificar_pagamento():
    dados = request.get_json()
    if not dados:
        return jsonify({"sucesso": False, "mensagem": "Dados inválidos."}), 400
        
    valor_texto = dados.get('valor')
    
    # Valida qual plano foi selecionado na interface
    if valor_texto == "29,99":
        dias_acesso = 7
        nome_plano = "Premium Inicial (7 Dias)"
        valor_float = 29.99
    elif valor_texto == "99,99":
        dias_acesso = 30
        nome_plano = "Premium Elite Pro (30 Dias)"
        valor_float = 99.99
    else:
        return jsonify({"sucesso": False, "mensagem": "Plano inválido."}), 400

    # Calcula o período em que o usuário terá acesso aos recursos
    data_expiracao = datetime.now() + timedelta(days=dias_acesso)
    expiracao_formatada = data_expiracao.strftime("%d/%m/%Y às %H:%M")
    
    # Atualiza os dados fictícios locais de teste
    USUARIO_LOGADO["plano_ativo"] = nome_plano
    USUARIO_LOGADO["expiracao_plano"] = expiracao_formatada

    try:
        # Grava a transação de forma permanente na tabela Pagamento do Banco de Dados
        novo_pagamento = Pagamento(
            usuario=USUARIO_LOGADO["username"],
            valor=valor_float,
            status="Pago"
        )
        db.session.add(novo_pagamento)
        db.session.commit()
        
        print(f"\n[BANCO DE DADOS] Transação salva! Plano {nome_plano} ativado para {USUARIO_LOGADO['username']}.\n")
        
    except Exception as e:
        db.session.rollback()
        print(f"\n[ERRO BANCO]: Falha ao salvar pagamento. Detalhes: {e}\n")

    return jsonify({
        "sucesso": True, 
        "mensagem": "Pagamento validado e gravado com sucesso!",
        "plano": USUARIO_LOGADO["plano_ativo"],
        "expira": USUARIO_LOGADO["expiracao_plano"]
    })


if __name__ == "__main__":
    porta = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=porta)
