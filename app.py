from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://cadastro_usuario_user:ZEeEUZKLOE21ZUprGPLy1rWlmD0S9DLx@dpg-cleo2lbl00ks739s9660-a/cadastro_usuario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Chave secreta para o Flask-Bcrypt
CORS(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    senha = db.Column(db.String(60), nullable=False)

@app.route('/pessoas', methods=['GET'])
def obter_pessoas():
    pessoas = Pessoa.query.all()
    if not pessoas:
        return jsonify({"mensagem": "Nenhuma pessoa cadastrada."})
    
    pessoas_json = [{"id": pessoa.id, "nome": pessoa.nome, "email": pessoa.email, "idade": pessoa.idade} for pessoa in pessoas]
    return jsonify({"pessoas": pessoas_json})

@app.route('/pessoas', methods=['POST'])
def cadastrar_pessoa():
    dados = request.json
    if not all(key in dados for key in ['nome', 'email', 'idade', 'senha']):
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    senha_hash = bcrypt.generate_password_hash(dados['senha']).decode('utf-8')

    nova_pessoa = Pessoa(nome=dados['nome'], email=dados['email'], idade=dados['idade'], senha=senha_hash)
    db.session.add(nova_pessoa)
    db.session.commit()
    return jsonify({"mensagem": "Pessoa cadastrada com sucesso!"})

@app.route('/pessoas/<int:pessoa_id>', methods=['DELETE'])
def excluir_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)
    if pessoa:
        db.session.delete(pessoa)
        db.session.commit()
        return jsonify({"mensagem": f"Pessoa com ID {pessoa_id} excluída com sucesso!"})
    else:
        return jsonify({"erro": f"Pessoa com ID {pessoa_id} não encontrada"}), 404

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    if not all(key in dados for key in ['email', 'senha']):
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    usuario = Pessoa.query.filter_by(email=dados['email']).first()

    if usuario and bcrypt.check_password_hash(usuario.senha, dados['senha']):
        return jsonify({"mensagem": "Login bem-sucedido!"})
    else:
        return jsonify({"erro": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True, use_reloader=False)  # Inicia o servidor Flask em modo de depuração
