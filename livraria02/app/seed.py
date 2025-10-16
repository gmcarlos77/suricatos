from main import app
from app import db
from models import Livro

def seed_livros():
    livros = [
        # Início
        {"isbn": "9780000000001", "titulo": "Assim falou Zaratustra", "autor": "Nietzsche", "genero": "Filosofia", "preco": "50,00", "rate": 4, "imagem": "zara.webp", "descricao": "Obra filosófica de Nietzsche", "tipo": "Capa comum"},
        {"isbn": "9780000000002", "titulo": "Memórias do Subsolo", "autor": "Dostoiévski", "genero": "Filosofia", "preco": "35,00", "rate": 4, "imagem": "subsolo.avif", "descricao": "Romance psicológico de Dostoiévski", "tipo": "Capa comum"},
        {"isbn": "9780000000003", "titulo": "Python e Django", "autor": "Luiz Eduardo Borges", "genero": "Programação", "preco": "85,00", "rate": 5, "imagem": "python.webp", "descricao": "Guia prático de Python e Django", "tipo": "Capa comum"},
        {"isbn": "9780000000004", "titulo": "As 48 Leis do Poder", "autor": "Robert Greene", "genero": "Não ficção", "preco": "120,00", "rate": 5, "imagem": "leis.jpg", "descricao": "Guia de poder e estratégia", "tipo": "Capa comum"},

        # Best-Sellers
        {"isbn": "9780000000010", "titulo": "1984", "autor": "George Orwell", "genero": "Distopia", "preco": "69,90", "rate": 4, "imagem": "1984.jpg", "descricao": "Distopia clássica", "tipo": "Capa comum"},
        {"isbn": "9780000000011", "titulo": "É Assim que Acaba", "autor": "Colleen Hoover", "genero": "Romance", "preco": "50,00", "rate": 4, "imagem": "assim-que-acaba.jpg", "descricao": "Romance intenso", "tipo": "Capa comum"},
        {"isbn": "9780000000012", "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil", "preco": "37,00", "rate": 5, "imagem": "pprincipe.jpeg", "descricao": "Clássico infantil", "tipo": "Capa comum"},
        {"isbn": "9780000000013", "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "genero": "Fábula", "preco": "50,00", "rate": 5, "imagem": "rev-bichos.jpeg", "descricao": "Fábula política", "tipo": "Capa comum"},

        # Literatura Clássica
        {"isbn": "9780000000020", "titulo": "Senhora", "autor": "José de Alencar", "genero": "Romance", "preco": "50,00", "rate": 4, "imagem": "senhora.jpeg", "descricao": "Romance clássico brasileiro", "tipo": "Capa comum"},
        {"isbn": "9780000000021", "titulo": "O Processo", "autor": "Franz Kafka", "genero": "Romance", "preco": "50,00", "rate": 4, "imagem": "processo.jpeg", "descricao": "Romance sobre burocracia", "tipo": "Capa comum"},
        {"isbn": "9780000000022", "titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "preco": "50,00", "rate": 5, "imagem": "domcas.jpeg", "descricao": "Clássico da literatura brasileira", "tipo": "Capa comum"},
        {"isbn": "9780000000023", "titulo": "Os Irmãos Karamazov", "autor": "Fiódor Dostoiévski", "genero": "Romance", "preco": "50,00", "rate": 5, "imagem": "irmaos.jpeg", "descricao": "Romance filosófico", "tipo": "Capa comum"},

        # Ficção
        {"isbn": "9780000000030", "titulo": "A Pedra Filosofal", "autor": "J.K. Rowling", "genero": "Fantasia", "preco": "50,00", "rate": 4, "imagem": "pedra-filosofal.jpeg", "descricao": "Início da saga Harry Potter", "tipo": "Capa comum"},
        {"isbn": "9780000000031", "titulo": "A Mão Esquerda de Deus", "autor": "Jeff Lindsay", "genero": "Crime", "preco": "50,00", "rate": 4, "imagem": "dexter.jpeg", "descricao": "História do serial killer Dexter", "tipo": "Capa comum"},
        {"isbn": "9780000000032", "titulo": "As Relíquias da Morte", "autor": "J.K. Rowling", "genero": "Fantasia", "preco": "50,00", "rate": 5, "imagem": "reliquias-harry.jpg", "descricao": "Último livro da saga Harry Potter", "tipo": "Capa comum"},
        {"isbn": "9780000000033", "titulo": "Sherlock Holmes", "autor": "Arthur Conan Doyle", "genero": "Mistério", "preco": "50,00", "rate": 5, "imagem": "sherlock.jpg", "descricao": "Detetive icônico", "tipo": "Capa comum"},

        # Não Ficção
        {"isbn": "9780000000040", "titulo": "Sapiens", "autor": "Yuval Noah Harari", "genero": "História", "preco": "50,00", "rate": 4, "imagem": "sapiens.jpeg", "descricao": "História da humanidade", "tipo": "Capa comum"},
        {"isbn": "9780000000041", "titulo": "Hábitos Atômicos", "autor": "James Clear", "genero": "Autoajuda", "preco": "50,00", "rate": 4, "imagem": "habitos-atomicos.jpeg", "descricao": "Pequenas mudanças, grandes resultados", "tipo": "Capa comum"},
        {"isbn": "9780000000042", "titulo": "Rápido e Devagar", "autor": "Daniel Kahneman", "genero": "Psicologia", "preco": "50,00", "rate": 5, "imagem": "rapido-devagar.jpeg", "descricao": "Exploração dos dois sistemas de pensamento", "tipo": "Capa comum"},
        {"isbn": "9780000000043", "titulo": "Nunca é Hora de Parar", "autor": "Chris Gardner", "genero": "Biografia", "preco": "50,00", "rate": 5, "imagem": "nunca-parar.jpeg", "descricao": "História de superação inspiradora", "tipo": "Capa comum"}
    ]

    for l in livros:
        if not Livro.query.get(l["isbn"]):
            livro = Livro(**l)
            db.session.add(livro)

    db.session.commit()
    print("Todos os livros fixos foram inseridos com sucesso!")

# Para rodar manualmente:
if __name__ == "__main__":
    with app.app_context():
        seed_livros()
