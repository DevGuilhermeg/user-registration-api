from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://cadastro_usuario_user:ZEeEUZKLOE21ZUprGPLy1rWlmD0S9DLx@dpg-cleo2lbl00ks739s9660-a/cadastro_usuario'
db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)

@app.route('/teste-conexao-bd', methods=['GET'])
def teste_conexao_bd():
    try:
        # Adiciona uma pessoa ao banco de dados
        nova_pessoa = Pessoa(nome="Exemplo", email="exemplo@email.com", idade=25)
        db.session.add(nova_pessoa)
        db.session.commit()

        return jsonify({"mensagem": "Conexão com o banco de dados bem-sucedida e registro adicionado."})
    except Exception as e:
        return jsonify({"erro": f"Erro na conexão com o banco de dados: {str(e)}"}), 500
