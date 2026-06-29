# routes/auth.py

from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint("auth", __name__)


@auth.route("/")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def fazer_login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    if email and senha:
        return redirect(url_for("dashboard"))

    return redirect(url_for("auth.login"))


@auth.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("auth.login"))
