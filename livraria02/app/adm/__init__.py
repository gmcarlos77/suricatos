from flask import Blueprint

adm_bp = Blueprint('adm', __name__, template_folder='templates', static_folder='../static')

from . import routes