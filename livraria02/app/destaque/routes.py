from flask import request, render_template
from . import destaque_bp
from models import Livro
from app import db


@destaque_bp.route("/", methods=["GET"])
def inicial():
    titulos = [
    "1984",
    "A Arte da Guerra",
    "As 48 Leis do Poder",
    "Assim Falou Zaratustra",
    "É Assim Que Acaba",
    "Um Curso de Cálculo – Volume 1",
    "Dexter: A Mão Esquerda de Deus",
    "Dom Casmurro",
    "Hábitos Atômicos"
]

    livros = Livro.query.filter(Livro.titulo.in_(titulos)).all()

    return render_template("inicial.html", livros=livros) 



@destaque_bp.route('/compra/<string:titulo>')
def tela_compra(titulo):
    livro = Livro.query.filter_by(titulo=titulo).first_or_404()
    return render_template("compra.html", livro=livro)

@destaque_bp.route('/livro/<string:genero>')
def livros_por_genero(genero):
    if genero == 'todos':
        livros_filtrados = Livro.query.all()  # Todos os livros
    else:
        livros_filtrados = Livro.query.filter(Livro.genero == genero).all()
    
    return render_template('inicial.html', livros=livros_filtrados)
