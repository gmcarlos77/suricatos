from flask import request, render_template

from models import Livro
from . import pesquisa_bp

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