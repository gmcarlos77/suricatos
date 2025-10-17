from flask import Blueprint

pesquisa_bp = Blueprint('pesquisa', __name__)

from . import routes