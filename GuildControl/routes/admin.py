# routes/admin.py

from flask import Blueprint, render_template, redirect, url_for

admin = Blueprint("admin", __name__)


@admin.route("/admin")
def painel_admin():
    return render_template("dashboard.html")


@admin.route("/admin/usuarios")
def usuarios():
    return render_template("perfil.html")


@admin.route("/admin/guildas")
def guildas():
    return render_template("guilda.html")


@admin.route("/admin/pagamentos")
def pagamentos():
    return render_template("pagamentos.html")


@admin.route("/admin/ranking")
def ranking():
    return render_template("ranking.html")


@admin.route("/admin/sair")
def sair():
    return redirect(url_for("auth.login"))
