from flask import render_template, request, flash, redirect, url_for
from . import adm_bp
from models import Livro
from app import db
from sqlalchemy.exc import IntegrityError

@adm_bp.route('/', methods=['GET','POST'])
def registro_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        descricao = request.form['descricao']
        genero = request.form['genero']
        isbn = request.form['isbn']
        preco = request.form['preco']
        imagem = request.form['imagem']
        ano = request.form['ano']


        generos = request.form.getlist('genero')
        genero = ', '.join(generos)

        livro = Livro(
            titulo=titulo,
            autor=autor,
            descricao=descricao,
            genero=genero,
            isbn=isbn,
            preco=preco,
            imagem=imagem,
            ano=ano
        )

        try:
            db.session.add(livro)
            db.session.commit()
            flash("Livro cadastrado com sucesso!")  # ← mensagem de sucesso
        except IntegrityError:
            db.session.rollback()
            flash("Erro: já existe um livro com esse ISBN!")  # ← mensagem de erro

        return redirect(url_for('adm.registro_livro'))

    # GET
    return render_template('adiconar_adm.html')

