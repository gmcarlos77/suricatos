from flask import render_template, request, redirect, url_for, flash, session
from main import app
from models import Usuario, Livro
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# ==========================
# 📚 PÁGINA INICIAL COM DESTAQUES E PESQUISA
# ==========================


# ==========================
# 🔑 LOGIN / REGISTRO / CONTA
# ==========================
@app.route("/telog", methods=["GET"])
def tela_login():
    return render_template("index.html")



@app.route("/home")
def home():
    if 'usuario_id' not in session:
        return redirect(url_for("tela_login"))
    return redirect(url_for("inicial"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("inicial"))


@app.route("/conta")
def conta():
    if 'usuario_id' not in session:
        session['next'] = url_for('conta')
        return redirect(url_for("tela_login"))

    usuario = Usuario.query.get(session['usuario_id'])
    return render_template("conta.html", nome=usuario.nome, email=usuario.email)


@app.route("/alterar_senha", methods=["POST"])
def alterar_senha():
    if 'usuario_id' not in session:
        flash("Você precisa estar logado.", "error")
        return redirect(url_for("tela_login"))

    usuario = Usuario.query.get(session['usuario_id'])

    senha_atual = request.form.get("senha_atual")
    nova_senha = request.form.get("nova_senha")
    confirma_senha = request.form.get("confirma_senha")

    if not check_password_hash(usuario.senha, senha_atual):
        flash("Senha atual incorreta.", "error")
        return redirect(url_for("conta"))

    if nova_senha != confirma_senha:
        flash("As novas senhas não conferem.", "error")
        return redirect(url_for("conta"))

    usuario.senha = generate_password_hash(nova_senha)
    db.session.commit()

    flash("Senha alterada com sucesso!", "success")
    return redirect(url_for("conta"))


# ==========================
# 🛒 COMPRA DE LIVRO
# ==========================
@app.route("/compra/<imagem>")
def tela_compra(imagem):
    # Busca livro pelo nome da imagem
    livro = Livro.query.filter_by(imagem=imagem).first()
    if not livro:
        flash("Livro não encontrado.", "error")
        return redirect(url_for("inicial"))
    
    return render_template("compra.html", livro=livro)
