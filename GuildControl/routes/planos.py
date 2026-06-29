# routes/planos.py

from flask import Blueprint, render_template, request, redirect, url_for

planos = Blueprint("planos", __name__)

# Chave pix do sistema
CHAVE_PIX = "ce023233@gmail.com"

@planos.route("/pagamentos")
def pagamentos():
    return render_template("pagamentos.html", chave_pix=CHAVE_PIX)
    


@planos.route("/plano/escolher", methods=["POST"])
def escolher_plano():
    plano = request.form.get("plano")

    if plano:
        return redirect(url_for("planos.pagamentos"))

    return redirect(url_for("planos.pagamentos"))


@planos.route("/plano/cancelar")
def cancelar_plano():
    return redirect(url_for("planos.pagamentos"))
