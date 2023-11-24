from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://cadastro_usuario_user:ZEeEUZKLOE21ZUprGPLy1rWlmD0S9DLx@dpg-cleo2lbl00ks739s9660-a/cadastro_usuario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    senha = db.Column(db.String(128), nullable=False)  # O comprimento padrão para o hash do Werkzeug

@app.route('/pessoas', methods=['GET'])
def obter_pessoas():
    pessoas = Pessoa.query.all()
    if not pessoas:
        return jsonify({"mensagem": "Nenhuma pessoa cadastrada."})
    
    pessoas_json = [{"id": pessoa.id, "nome": pessoa.nome, "email": pessoa.email, "idade": pessoa.idade} for pessoa in pessoas]
    return jsonify({"pessoas": pessoas_json})



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True, use_reloader=False)  # Inicia o servidor Flask em modo de depuração
