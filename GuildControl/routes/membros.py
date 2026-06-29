# routes/membros.py

from flask import Blueprint, render_template, request, redirect, url_for

membros = Blueprint("membros", __name__)


@membros.route("/membros")
def listar_membros():
    return render_template("ranking.html")


@membros.route("/membros/adicionar", methods=["POST"])
def adicionar_membro():
    nick = request.form.get("nick")
    line = request.form.get("line")

    if nick and line:
        return redirect(url_for("membros.listar_membros"))

    return redirect(url_for("membros.listar_membros"))


@membros.route("/membros/remover/<int:id>")
def remover_membro(id):
    return redirect(url_for("membros.listar_membros"))
