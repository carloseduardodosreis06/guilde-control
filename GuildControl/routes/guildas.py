# routes/guildas.py

from flask import Blueprint, render_template, request, redirect, url_for

guildas = Blueprint("guildas", __name__)


@guildas.route("/guilda")
def pagina_guilda():
    return render_template("guilda.html")


@guildas.route("/guilda/criar", methods=["POST"])
def criar_guilda():
    nome = request.form.get("nome")

    if nome:
        return redirect(url_for("guildas.pagina_guilda"))

    return redirect(url_for("guildas.pagina_guilda"))


@guildas.route("/guilda/excluir/<int:id>")
def excluir_guilda(id):
    return redirect(url_for("guildas.pagina_guilda"))
