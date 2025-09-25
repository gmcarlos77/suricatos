from flask import render_template, request, redirect, url_for, flash, session
from main import app
from models import Usuario
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/", methods=["GET"])
def tela_login():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
        flash("Usuário não existe. Por favor, registre-se.", "error")
        return redirect(url_for("tela_login"))

    if not check_password_hash(usuario.senha, senha):
        flash("Senha incorreta.", "error")
        return redirect(url_for("tela_login"))

    # Login OK
    session['usuario_id'] = usuario.id
    session['usuario_nome'] = usuario.nome
    return redirect(url_for("home"))

@app.route("/registro", methods=["POST"])
def registro():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    confirma_senha = request.form.get("confirma_senha")

    if senha != confirma_senha:
        flash("As senhas não conferem.", "error")
        return redirect(url_for("tela_login"))

    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        flash("Email já cadastrado.", "error")
        return redirect(url_for("tela_login"))

    nova_senha = generate_password_hash(senha)

    novo_usuario = Usuario(nome=nome, email=email, senha=nova_senha)
    db.session.add(novo_usuario)
    db.session.commit()

    # Loga o usuário após o registro
    session['usuario_id'] = novo_usuario.id
    session['usuario_nome'] = novo_usuario.nome

    return redirect(url_for("home"))

@app.route("/home")
def home():
    if 'usuario_id' not in session:
        return redirect(url_for("tela_login"))
    return render_template("inicial.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("tela_login"))
