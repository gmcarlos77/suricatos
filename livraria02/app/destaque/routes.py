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



