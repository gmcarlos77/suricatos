from datetime import datetime
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
    
class Livro(db.Model):
    isbn = db.Column(db.String(13), primary_key=True) 
    titulo = db.Column(db.String(150), nullable=False)
    autor = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    preco = db.Column(db.String(20))
    imagem = db.Column(db.String(200))
    descricao = db.Column(db.Text)
    ano = db.Column(db.String(6))

