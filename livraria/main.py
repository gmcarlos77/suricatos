from flask import Flask
import os
from extensions import db

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # importante para sessão e flash

base_dir = os.path.abspath(os.path.dirname(__file__))

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "models.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Importa rotas depois de configurar o app e o banco
from rotas import *


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
