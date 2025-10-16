from flask import Blueprint

destaque_bp = Blueprint('destaque', __name__, template_folder='templates', static_folder='../static')
from . import routes
