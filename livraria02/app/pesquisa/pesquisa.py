from flask import Blueprint, render_template, request
from models import Livro

pesquisa_bp = None
@pesquisa_bp.route("/pesquisar", methods=["GET"])
def pesquisar():
    termo = request.args.get("q", "").strip()  # pega o termo da pesquisa
    resultados = []

    if termo:
        # Busca pelo título ou autor
        resultados = Livro.query.filter(
            (Livro.titulo.ilike(f"%{termo}%")) |
            (Livro.autor.ilike(f"%{termo}%"))
        ).all()

    return render_template("resultado_pesquisa.html", resultados=resultados, termo=termo)