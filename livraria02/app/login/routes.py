from flask import Blueprint, request, session, flash, redirect, url_for, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from models import Usuario
from app import db
from . import login_bp


# ==============================
# 🔑 LOGIN
# ==============================
@login_bp.route("/telog", methods=["GET"])
def tela_login():
    return render_template("index.html")


@login_bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
        flash("Usuário não existe. Por favor, registre-se.", "error")
        return redirect(url_for("login.tela_login"))

    if not check_password_hash(usuario.senha, senha):
        flash("Senha incorreta.", "error")
        return redirect(url_for("login.tela_login"))

    session['usuario_id'] = usuario.id
    session['usuario_nome'] = usuario.nome

    next_page = session.pop('next', None)
    return redirect(next_page or url_for("destaque.inicial"))


# ==============================
# 🧾 REGISTRO
# ==============================
@login_bp.route("/registro", methods=["POST"])
def registro():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    confirma_senha = request.form.get("confirma_senha")

    if senha != confirma_senha:
        flash("As senhas não conferem.", "error")
        return redirect(url_for("login.tela_login"))

    if Usuario.query.filter_by(email=email).first():
        flash("Email já cadastrado.", "error")
        return redirect(url_for("login.tela_login"))

    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha=generate_password_hash(senha)
    )
    db.session.add(novo_usuario)
    db.session.commit()

    session['usuario_id'] = novo_usuario.id
    session['usuario_nome'] = novo_usuario.nome

    return redirect(url_for("destaque.inicial"))
