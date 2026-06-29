# routes/pontuacoes.py

from flask import Blueprint, render_template, request, redirect, url_for

pontuacoes = Blueprint("pontuacoes", __name__)


@pontuacoes.route("/ranking")
def ranking():
    return render_template("ranking.html")


@pontuacoes.route("/pontuacao/adicionar", methods=["POST"])
def adicionar_pontuacao():
    jogador = request.form.get("jogador")
    pontos = request.form.get("pontos")

    if jogador and pontos:
        return redirect(url_for("pontuacoes.ranking"))

    return redirect(url_for("pontuacoes.ranking"))


@pontuacoes.route("/pontuacao/remover/<int:id>")
def remover_pontuacao(id):
    return redirect(url_for("pontuacoes.ranking"))
